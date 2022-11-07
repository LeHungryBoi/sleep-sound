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
 
silent_interval_min = 69
silent_interval_max = 189
time_begin = "2048"
time_peak = "0300"
time_over = "0812"
force_1 = False

booming_time = False
boom_burst_count = 0
boom_burst_min = 1
boom_burst_max = 3
boom_burst_amount = 1
hold_on_time_min = 0.2
hold_on_time_max = 1.2
hold_on_time_amount = 0

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', default=False, action='store_true', help='force noise when not at booming time')
parser.add_argument('-d', '--debug', default=False, action='store_true', help='short silent interval for debugging')
args = parser.parse_args()


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
  
def SetVolume():
  r = random.randint(50, 100)
  return r

def ReturnPathToRandomAudio ():
  randomfile = random.choice(os.listdir(music_dir))
  print ("Playing file" ,randomfile,"...")
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
  s = ReturnAPRandomAudio()
  ap = AudioPlayer(s)
  v = SetVolume()
  ap.volume = v
  ap.play(loop=False, block=True)

def ParseArgument():
  global args
  print(args.force)
  print(args.debug)
  global force_1
  if(args.force):
    force_1 = True
    print("force is True")
  else:
    force_1 = False
    print("force is False")
  if(args.debug):
    global silent_interval_min
    global silent_interval_max
    silent_interval_min = 1
    silent_interval_max = 2
    print("short silent interval")
  else:
    pass

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
  while True:
    SetBoomingTime()
    if(force_1 == True):
      PlayRandomSound()

    while(booming_time or force_1):
      SL = SetSilentInterval()
      sleep(SL)
      boom_burst_amount = random.randint(boom_burst_min, boom_burst_max)
      while(boom_burst_count < boom_burst_amount):
        PlayRandomSound()
        #os.system('aplay -D hw:CARD=D1,DEV=0 ' + s)
        print("boom")
        boom_burst_count += 1
        print(boom_burst_count, "/", boom_burst_amount)
        hold_on_time_amount = random.uniform(hold_on_time_min, hold_on_time_max)
        print("hold on ", hold_on_time_amount)
        sleep(hold_on_time_amount) 
      else:
        boom_burst_count = 0
    sleep(.5)

