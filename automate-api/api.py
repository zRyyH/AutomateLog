from keyboard_monitor import KeyLogger
from manager import Manager
from orm import get_fretes
import time


StradaBOT = Manager()
Keyboard = KeyLogger(manager=StradaBOT)
Keyboard.run()


while True:
    try:
        time.sleep(1)
        
        filtros_definidos = get_fretes()
        StradaBOT.filters = filtros_definidos
    except:
        print('PROBLEMA NO BANCO DE DADOS!')