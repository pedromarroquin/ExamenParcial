import pynput.keyboard
from datetime import datetime,time
import timeit

class tiempos:
    count=0

    def pressKey(self, key):
        if self.count==0:
            print("La tecla",key,"se presiono:",str(datetime.today()))
        self.count=self.count+1

    def leaveKey(self, key):
        print("La tecla",key,"se soltó:",str(datetime.today()))
        self.count=0
   
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(self.pressKey, self.leaveKey)
        with keyboard_listener:
            keyboard_listener.join()
