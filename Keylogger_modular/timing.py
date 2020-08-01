from pynput.keyboard import Listener
from datetime import datetime,time

class tiempos:
    count=0
    log =""
    
    def appendLog(self,string):
        self.log = self.log + string
        print(self.log)
        
    def recognize(self, key):
            try:
                otrokey = str(key.char)
            except AttributeError:
                if key == key.space:
                    otrokey = " "
                else:
                    otrokey= " " + str(key) + " " 
            self.appendLog(otrokey)

    def pressKey(self, key):
        self.recognize(key)
        if self.count==0:
            print("La tecla",key,"se presiono:",str(datetime.today()))
        self.count=self.count+1

    def leaveKey(self, key):
        print("La tecla",key,"se soltó:",str(datetime.today()))
        self.count=0
   
    def start(self):
        keyboard_listener = Listener(self.pressKey, self.leaveKey)
        with keyboard_listener:
            keyboard_listener.join()

