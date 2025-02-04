import keyboard

class KeyLogger:
    def __init__(self, manager):
        self.manager = manager

    def key_event(self, key):
        if key.name == "/":
            print('Ligando Sistema!')
            self.manager.start()
            print('Sistema Ligado!')

        elif key.name == "*":
            print('Desligando Sistema...')
            self.manager.stop()
            print('Sistema Desligado!')

    def run(self):
        keyboard.on_press(self.key_event)