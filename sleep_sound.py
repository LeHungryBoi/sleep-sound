#!/usr/bin/env python
from datetime import datetime
import os, random, sys, select
from time import sleep, strptime
from sound_go_boom_class import soundgoboom 


running_dir = os.path.dirname(__file__)
music_dir = os.path.join(running_dir, 'music')
 
time_min = 69
time_max = 189
time_begin = 2048
time_over = 812
booming_time = False
force_1 = False
boom_burst_count = 0
boom_burst_min = 1
boom_burst_max = 4
boom_burst_amount = 1
boom_burst_interval_min = 0.2
boom_burst_interval_max = 1.2
boom_burst_interval_amount = 0


def GetCurrentTIme():
  full_datetime = datetime.now()
  raw_datetime = full_datetime.strftime('%H%M')
  good_datetime = int(raw_datetime)
  return good_datetime

def BoomerScheduler():
  global booming_time
  global boom_burst_amount
  global boom_burst_interval_amount
  global boom_burst_interval_min
  global boom_burst_interval_max

  current_time = GetCurrentTIme()
  if (current_time > time_over and current_time < time_begin):
    booming_time = False
  elif(current_time > time_begin or current_time < time_over ):
    booming_time = True

  boom_burst_amount = random.randint(boom_burst_min, boom_burst_max)
  boom_burst_interval_amount = random.uniform(boom_burst_interval_min, boom_burst_interval_max)
  

def SelectRandomAudio ():
  randomfile = random.choice(os.listdir(music_dir))
  print ("Playing file" ,randomfile,"...")
  rmusic_file = os.path.join(music_dir, randomfile)
  return rmusic_file

def GoBoom():
  if (booming_time or force_1):
    music_file = SelectRandomAudio()
    print(music_file)
    soundgoboom.SoundGoBoom(music_file)
    print("BOOM")

def SetSilentInterval():
  p = random.randint(time_min, time_max)
  print("Waiting for", p, "seconds")
  return p


if (__name__ == "__main__"):
  #force_1 = sys.argv[1]
  while True:
    #print(running_dir)
    #print(music_dir)
    BoomerScheduler()
    print(booming_time)

    while (boom_burst_count < boom_burst_amount):
      m = SelectRandomAudio()
      if(booming_time or force_1 == 1):
        os.system('aplay ' + m)
        print("BOOM")
        
      
      boom_burst_count += 1

      print(boom_burst_count, "/", boom_burst_amount)
      print("hold on ", boom_burst_interval_amount)
      sleep(boom_burst_interval_amount)
      
    else:
      boom_burst_count = 0

    SL = SetSilentInterval()
    sleep(SL)
    sleep(1)

