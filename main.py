#from turtle import onclick
import pyautogui
from pynput.mouse import Button, Controller, Listener
from pynput import mouse
import time
#import logging

#my_file = open("script.py", "w")
#my_file.write("test123")
#logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')
#def on_move(x, y):
#    logging.info("Mouse moved to ({0}, {1})".format(x, y))
#def on_scroll(x, y, dx, dy):
#    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))


def on_click(x, y, button, pressed):
    if pressed:
        #logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        with open("script.py", "a") as my_file:
            my_file.write('({0}, {1}) {2}\n'.format(x, y, button))
            my_file.write(time.strftime("%M %S\n", time.localtime()))
            print(my_file.name)
            my_file.write("test")
            my_file.close()
     

    
        
        

with Listener(on_click=on_click) as listener:
    listener.join()


