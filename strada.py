from actions import refresh, check_ofertas, solicitar, confirmar, rolagem
import threading
import time


class StradaLog:
    def __init__(self):
        self.running = False
        self.settings = []


    def set_settings(self, payload):
        self.settings = payload


    def start_stop(self, state):
        self.running = state
    

    def loop(self):
        while True:
            try:
                if self.running:
                    time.sleep(1)
                    ofertas = check_ofertas()
                    for oferta in ofertas:
                        for setting in self.settings:
                            isOrigem1 = oferta['origem_1'] == setting['text1']
                            isOrigem2 = oferta['origem_2'] == setting['text2']
                            
                            if isOrigem1 and isOrigem2:
                                solicitar(element=oferta['oferta'])
                                print(oferta)
                    refresh()
            except Exception as e:
                print(e)


    def run_loop(self):
        # Criando e iniciando a thread
        thread = threading.Thread(target=self.loop)
        thread.start()