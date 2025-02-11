from keyboard_monitor import KeyLogger
from orm import get_fretes, get_status
from manager import Manager
import time


StradaBOT = Manager()
Keyboard = KeyLogger(manager=StradaBOT)
Keyboard.run()


while True:
    try:
        time.sleep(1)

        filtros_definidos = get_fretes()
        configuracoes = get_status()

        if configuracoes['status'] == 0 and StradaBOT.running == 1:
            StradaBOT.stop()
            print('DESLIGADO')
            
        elif configuracoes['status'] == 1 and StradaBOT.running == 0:
            StradaBOT.start()
            print('LIGADO')

        StradaBOT.filters = filtros_definidos
    except Exception as e:
        print('PROBLEMA NO BANCO DE DADOS!', e)