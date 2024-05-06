from kivy.clock import Clock
import serial
import sys


# Constants and global state variables
font_size = 20
system = 0
arm = 0
alarm = 0
alarm_start_time = 0
face_id = 0
recording = 0

def set_alarm(state):
    global alarm
    alarm = state

def get_alarm():
    return alarm


