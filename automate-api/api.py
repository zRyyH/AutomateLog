from keyboard_monitor import KeyLogger
from manager import Manager
from orm import get_fretes, get_status
import time


StradaBOT = Manager()
Keyboard = KeyLogger(manager=StradaBOT)
Keyboard.run()


while True:
    try:
        time.sleep(1)

        filtros_definidos = get_fretes()
        configuracoes = get_status()

        if configuracoes['status'] == 0:
            StradaBOT.stop()
            print('DESLIGADO')
        else:
            StradaBOT.start()
            print('LIGADO')

        StradaBOT.filters = filtros_definidos

    except Exception as e:
        print('PROBLEMA NO BANCO DE DADOS!', e)