# Assignment 10

# Contact Tracing App
# 	- Create a python program that will read QRCode using your webcam
# 	- You may use any online QRCode generator to create QRCode
# 	- All personal data are in QRCode 
# 	- You may decide which personal data to include
# 	- All data read from QRCode should be stored in a text file including the date and time it was read

# Note: 
# 	- Search how to generate QRCode
# 	- Search how to read QRCode using webcam
# 	- Search how to create and write to text file
# 	- Your source code should be in github before Feb 19
# 	- Create a demo of your program (1-2 min) and send it directly to my messenger

import webbrowser
import cv2
# Installed pip openCv for cv2

import datetime
import time
# Imported the datetime and time module for the Real time Management System

def time_(icon):
    local_time = datetime.now() 
    datezone = local_time.strftime("%B %d, %Y") 
    current_time = time.localtime() 
    timezone = time.strftime("%H:%M", current_time) 
    timezoneNUM = int(time.strftime("%H", current_time)) 
    timezoneDate = time.strftime("%M", current_time) 
    hour_clock = 12
    with open(information, "w") as update:
        if timezoneNUM >= 0 and timezoneNUM < hour_clock:
            update.write (f"\n\n>>> REAL-TIME MANAGEMENT SYSTEM <<< \nDate Recorded: {datezone}\nTime Recorded: {timezone} AM")
        else:
            timeCurrent = (timezoneNUM) - hour_clock
            update.write (f"\n\n>>> REAL-TIME MANAGEMENT SYSTEM <<< \nDate Recorded: {datezone}\nTime Recorded: {timeCurrent}:{timezoneDate} PM")
    return icon; 

information = "Student_Information.txt"


