#python3
from datetime import datetime
import os, random, sys, select
from time import sleep, strptime

def SetContinuousTime():
    int = int(i)

full_datetime = datetime.now()
raw_datetime = full_datetime.strftime('%H%M')
good_datetime = int(raw_datetime)
print(raw_datetime)
print(good_datetime)
i = datetime.now().strftime('%H%M')
print(i)
int = int(i)
print(int)
