from pynput.mouse import Button, Controller, Listener
from pynput import mouse
import time
#import data.py

class Data():
    x_cord = 0
    y_cord = 0
    time = 0

    def __init__(self,x_cord, y_cord, time):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.time = time
    
    def get_x(self):
        return self.x_cord

    def get_y(self):
        return self.y_cord

    def get_time(self):
        return self.time


    
def GetTimeMinutes(str):
    raw = str.split(',')
    return raw[3]

def GetTimeSeconds(str):
    raw = str.split(',')
    return raw[4]




raw_time = time.strftime("0,0,0,%M,%S", time.localtime())
start_time_minutes = GetTimeMinutes(raw_time)
start_time_seconds = GetTimeSeconds(raw_time)
event_data = []

def ParseX(str):
    raw = str.split(',')
    x = raw[0]
    return x

def ParseY(str):
    raw = str.split(',')
    y = raw[1]
    return y


def ParseTime(str,last_time_minutes, last_time_seconds):
    raw = str.split(',')
    raw_minutes = raw[3]
    raw_seconds = raw[4]
    minutes = int(raw_minutes) - int(last_time_minutes)
    seconds = int(raw_seconds) - int(last_time_seconds)
    final_time = (minutes * 60) + seconds
    return final_time

def on_click(x, y, button, pressed):
    if pressed:
        global start_time_seconds
        global start_time_minutes
        data = '{0}, {1}, {2},'.format(x, y, button) + time.strftime("%M,%S", time.localtime())
        x = ParseX(data)
        y = ParseY(data)
        time_spend = ParseTime(data, start_time_minutes, start_time_seconds)
        start_time_minutes = GetTimeMinutes(data)
        start_time_seconds = GetTimeSeconds(data)
        obj = Data(x, y, time_spend)
        event_data.append(obj)
        print_objects()


def print_objects():
    print("Start time minutes and seconds:" + str(start_time_minutes) + "," + str(start_time_seconds))
    for i in event_data:
        print(i.get_x(), i.get_y(), i.get_time())
    
    print("\n")



'''    
raw_data = "1698,380,Button.left,25,38"
current_time_mintues = "24"
current_time_seconds = "36"
print(ParseX(raw_data))
print(ParseY(raw_data))
print(ParseTime(raw_data, current_time_mintues, current_time_seconds))
'''

with Listener(on_click=on_click) as listener:
    listener.join()


