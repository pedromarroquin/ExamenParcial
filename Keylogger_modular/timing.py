from pynput.keyboard import Listener
from datetime import datetime,time
from os.path import isfile
import threading
import report

class tiempos:
    count=0
    log =""
    captcha=""
    keyword=""
    inicio=""
    fin=""
    txt=""
    def appendLog(self,string):
        self.log = self.log + string
        print(self.log)
        
    def recognize(self, key):
            try:
                otrokey = str(key.char)
                self.keyword=otrokey
            except AttributeError:
                if key == key.space:
                    otrokey = " "
                else:
                    otrokey= " " + str(key) + " " 
            self.appendLog(otrokey)
    
    def pressRecord(self,rt):
        self.captcha=self.keyword+"\t\t\t"+self.inicio+"\t\t"+self.fin
        rt.timing(self.captcha,rt.setName())
        self.captcha=""

    def pressKey(self, key):
        self.recognize(key)
        if self.count==0:
            self.inicio=str(datetime.today())
        self.count=self.count+1

    def leaveKey(self, key):
        self.fin=str(datetime.today())
        self.pressRecord(self.txt)
        self.count=0

    
    def start(self,repoTiming):
        self.txt=repoTiming
        keyboard_listener = Listener(self.pressKey, self.leaveKey)
        with keyboard_listener:
            keyboard_listener.join()
