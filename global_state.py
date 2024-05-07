from kivy.clock import Clock
import serial
import sys
from face_id.authentication import authenticate
from screen_reader import translations

# global_state.py

# Import necessary libraries if required (e.g., for saving settings)
import json

# Initial global state variables
language = 'English'  # Default language
font_size = 20
system = 1
arm = 1
alarm_triggered =1
alarm = 0
alarm_start_time = 0
face_id = 0
recording = 0

# Function to set the current language
def set_language(new_language):
    global language
    language = new_language
    # Here you can add code to save this setting to a file or database if needed

# Function to get the current language
def get_language():
    return language

def get_translation(language, key):
    # Fetch the dictionary for the current language and retrieve the key
    return translations.get(language, {}).get(key, "Translation not found")

def set_alarm(state):
    global alarm
    alarm = state

def get_alarm():
    return alarm
