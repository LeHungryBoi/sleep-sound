#!/usr/bin/env python
from datetime import datetime
import os, random, sys, select
from time import sleep, strptime
from sound_go_boom_class import soundgoboom 
import argparse
import configparser
from audioplayer import AudioPlayer


running_dir = os.path.dirname(__file__)
music_dir = os.path.join(running_dir, 'music')
 
silent_interval_min = 900
silent_interval_max = 1200
time_begin = "2148"
time_over = "0812"
time_peak = "0300"
force_1 = False

booming_time = False
boom_burst_count = 0
boom_burst_min = 1
boom_burst_max = 1
boom_burst_amount = 0
rythmic_pause_min = 0.2
rythmic_pause_max = 0.4
rythmic_pause_amount = 0

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', default=False, action='store_true', help='force noise when not at booming time')
parser.add_argument('-i', '--interval', default=False, action='store_true', help='short silent interval for debugging')
parser.add_argument('--ap', default=False, action='store_true', help='use audioplayer library')
parser.add_argument('-b', '--begin', default=None, help='begining time of boom')
parser.add_argument('-o', '--over', default=None, help='over time of boom')
parser.add_argument('--rmin', default=None, help='rythmic pause minimum')
parser.add_argument('--rmax', default=None, help='rythmic pause maximum')
parser.add_argument('--smin', default=None, help='silent interval minimum')
parser.add_argument('--smax', default=None, help='silent interval maximum')
args = parser.parse_args()

ap = False
config = configparser.ConfigParser()

def GetCurrentTimeInt():
  #full_datetime = datetime.now()
  #raw_datetime = full_datetime.strftime('%H%M')
  good_datetime = int(datetime.now().strftime('%H%M'))
  return good_datetime

def SetContinuousTime():
  if (time_over < time_begin):
    temp_time_begin = time_begin
    temp_time_over = time_over + 2400


def SetBoomingTime():
  global booming_time
  global boom_burst_amount

  current_time_int = GetCurrentTimeInt()
  time_begin_int = int(time_begin)
  time_over_int = int(time_over)
  if(time_begin_int < time_over_int): #in one day
    if (current_time_int > time_begin_int and current_time_int < time_over_int):#one day
      booming_time = True
    else:
      booming_time = False
  elif(time_begin_int > time_over_int): #across two day
    if(current_time_int > time_over_int and current_time_int < time_begin_int):
      booming_time = False
    else:
      booming_time = True
  else:
    booming_time = True
  if(booming_time):
    print("booming time")
  else:
    print("silent time")
  
def SetVolume(min = 50.0, max = 100.0):
  r = random.uniform(min, max)
  return r

def ReturnPathToRandomAudio ():
  randomfile = random.choice(os.listdir(music_dir))
  print ("Selected " ,randomfile)
  rmusic_file = os.path.join(music_dir, randomfile)
  return rmusic_file

def ReturnAPRandomAudio():
  randomfile = random.choice(os.listdir(music_dir))
  return("music/" + randomfile)

def GoBoom():
  if (booming_time or force_1):
    music_file = ReturnPathToRandomAudio()
    print(music_file)
    soundgoboom.SoundGoBoom(music_file)
    print("BOOM")

def SetSilentInterval():
  p = random.randint(silent_interval_min, silent_interval_max)
  print("Waiting for", p, "seconds")
  return p

def PlayRandomSound():
  global ap
  if(ap):
    s = ReturnPathToRandomAudio()
    ap = AudioPlayer(s)
    v = SetVolume()
    ap.volume = v
    ap.play(loop=False, block=True)
  else:
    s = ReturnPathToRandomAudio()
    v = SetVolume(0.8, 1.2)
    os.system('play -v ' + str(v) + " " + s)
  print("boom")

def ParseArgument():
  global args
  global force_1
  if(args.force):
    force_1 = True
    print("force is True")
  else:
    force_1 = False
    print("force is False")
  if(args.interval):
    global silent_interval_min
    global silent_interval_max
    global rythmic_pause_min
    global rythmic_pause_max
    silent_interval_min = 1
    silent_interval_max = 2
    rythmic_pause_min = 0.2
    rythmic_pause_max = 0.4
    print("short silent interval")
  else:
    pass
  if(args.ap):
    global ap
    ap = True

  if(args.begin != None):
    global time_begin
    time_begin = args.begin
  if(args.over != None):
    global time_over
    time_over = args.over

  if(args.rmin):
    rythmic_pause_min = float(args.rmin)

  if(args.rmax != None):
    rythmic_pause_max = float(args.rmax)

  if(args.smin != None):
    silent_interval_min = int(args.smin)
  if(args.smax != None):
    silent_interval_max = int(args.smax)

def ParseConfig():
  config['DEFAULT'] = {'ServerAliveInterval': '45',
                       'Compression': 'yes',
                       'CompressionLevel': '9'}

  config['bitbucket.org'] = {}
  config['bitbucket.org']['User'] = 'hg'

  config['topsecret.server.com'] = {}
  topsecret = config['topsecret.server.com']
  topsecret['Port'] = '50022'     # mutates the parser
  topsecret['ForwardX11'] = 'no'  # same here

  config['DEFAULT']['ForwardX11'] = 'yes'

  with open('boom_config.ini', 'w') as configfile:
    config.write(configfile)

def RandomBoom(probability):
  return random.randrange(0, 100) > probability



if (__name__ == "__main__"):
  ParseArgument()
  if(force_1 == True):
      PlayRandomSound()
  while True:
    SetBoomingTime()
    if(booming_time or force_1):
      SL = SetSilentInterval()
      print("sleeping for ", SL)
      sleep(SL)
      #Silent Interval(Long Stop) between sound

      boom_burst_amount = random.randint(boom_burst_min, boom_burst_max)
      #randomly set how many burst

      while(boom_burst_count < boom_burst_amount):
        will = RandomBoom(40)
        if(will):
          PlayRandomSound()
        boom_burst_count += 1
        if(will):
          print(boom_burst_count, "/", boom_burst_amount)
        rythmic_pause_amount = random.uniform(rythmic_pause_min, rythmic_pause_max) 
        if(will):
          print("hold on ", rythmic_pause_amount)
        if(not will):
          print("it's a dud")
        sleep(rythmic_pause_amount) 
      else:
        boom_burst_count = 0
    sleep(1)

