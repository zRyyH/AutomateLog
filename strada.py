from actions import refresh, check_ofertas, solicitar, confirmar, rolagem
import threading
import time


class StradaLog:
    def __init__(self):
        self.running = False
        self.settings = {
            "origens_1": [],
            "origens_2": []
        }


    def set_settings(self, payload):
        self.settings.update(payload)


    def start_stop(self, state):
        self.running = state
    

    def loop(self):
        while True:
            if self.running:
                time.sleep(1)
                ofertas = check_ofertas()
                print(ofertas)
                

    def run_loop(self):
        # Criando e iniciando a thread
        thread1 = threading.Thread(target=self.loop)
        thread1.start()