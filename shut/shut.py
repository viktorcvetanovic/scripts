#program za gasenje pc
import os
from tkinter import *
import tkinter
import tkinter as Tk
import time
import sys


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        if t==1:
            os.system("shutdown /s /t 1")

def print_start_time( a, b):
    print("Minutes: "+str(a))
    print("Seconds: "+str(b))
    print("\n")

args=sys.argv

if(len(args)==2):
    t=(int(args[1])*60)
    print_start_time(args[1],0)
    countdown(t)
elif(len(args)==3): 
    t=(int(args[1])*60)+int(args[2])
    print_start_time(args[1],args[2])
    countdown(t)
else:
    print("Please enter minutes and | or seconds")
    

