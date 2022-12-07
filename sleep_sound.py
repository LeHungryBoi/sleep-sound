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
time_begin = "2348"
time_over = "0512"
time_peak = "0300"
force_1 = False

booming_time = False
boom_burst_count = 0
boom_burst_min = 1
boom_burst_max = 1
boom_burst_amount = 0
hold_on_time_min = 0.2
hold_on_time_max = 0.4
hold_on_time_amount = 0

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', default=False, action='store_true', help='force noise when not at booming time')
parser.add_argument('-i', '--interval', default=False, action='store_true', help='short silent interval for debugging')
parser.add_argument('--ap', default=False, action='store_true', help='use audioplayer library')
parser.add_argument('-b', '--begin', default=None, help='begining time of boom')
parser.add_argument('-o', '--over', default=None, help='over time of boom')
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
  global hold_on_time_amount
  global hold_on_time_min
  global hold_on_time_max

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
    global hold_on_time_min
    global hold_on_time_max
    silent_interval_min = 1
    silent_interval_max = 2
    hold_on_time_min = 0.2
    hold_on_time_max = 0.4
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
        PlayRandomSound()
        boom_burst_count += 1
        print(boom_burst_count, "/", boom_burst_amount)
        hold_on_time_amount = random.uniform(hold_on_time_min, hold_on_time_max) # change hold_on_time to rythmic pause
        print("hold on ", hold_on_time_amount)
        sleep(hold_on_time_amount) 
      else:
        boom_burst_count = 0
    sleep(1)

