import pyautogui
#import grab_data
import time
f = open("script.py", "w")
def make_click(x,y):
    # Write pyautogui.click(x,y) to file put replace x and y with numbers from event data 
    global f
    f.write("pyautogui.click(")
    x = str(x)
    f.write(x)
    f.write(",")
    y = str(y)
    f.write(y)
    f.write(")\n")

def make_sleep(sleep):
    global f
    f.write("time.sleep(")
    sleep = str(sleep)
    f.write(sleep)
    f.write(")\n")


def init():
    global f
    f.write("import pyautogui\n")
    f.write("import time\n")


f.close()