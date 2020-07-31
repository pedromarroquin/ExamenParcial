from datetime import datetime

class report:
    z = datetime.now()
    m = "keylogger_fecha_{}.txt".format(z.strftime("%d-%m-%Y_%H-%M-%S"))
    #¿Creamos txt para cada uno?

    def __init__(self, rarch, rtiming, rcount):
        self.rarch = rarch
        self.rtiming = rtiming
        self.rcount = rcount

    def crearTXT(self,captexto):
        archivo = open(self.m,"w+")
        archivo.write(captexto)
        archivo.close()

    