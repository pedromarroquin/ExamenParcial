import pynput.keyboard
from datetime import datetime,time
import timeit

count=0

def pressKey(key):
    global count
    if count==0:
        print("La tecla",key,"se presiono:",str(datetime.today()),"",str(timeit.timeit()*1000)," ms")
    count=count+1

def leaveKey(key):
    global count
    print("La tecla",key,"se soltó:",str(datetime.today()),"",str(timeit.timeit()*1000)," ms")
    count=0
keyboard_listener=pynput.keyboard.Listener(pressKey,leaveKey)
with keyboard_listener:
    keyboard_listener.join() 
