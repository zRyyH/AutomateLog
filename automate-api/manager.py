from services import validar_oferta, status_lista
from appium_driver import AppiumDriver
from state_monitor import StateMonitor
from actions import Actions

import threading
import time


class Manager:
    def __init__(self):
        self.AppiumDriver = AppiumDriver()
        self.StateMonitor = StateMonitor(AppiumDriver=self.AppiumDriver)
        self.Actions = Actions(AppiumDriver=self.AppiumDriver)

        self.thread_loop = None
        self.running = False
        self.filters = []

    def get_ofertas(self):
        return self.StateMonitor.ofertas_state()

    def get_state_lista(self, ofertas=None):
        if ofertas != None:
            return status_lista(ofertas=ofertas)
        else:
            return status_lista(ofertas=self.get_ofertas())

    def resetar_lista(self):
        print("RESETANDO LISTA")
        try:
            while self.get_state_lista() != "COMECO_DA_LISTA":
                print("VOLTANDO PARA O INICIO DA LISTA")
                self.Actions.scroll(scroll_value=10000)
                time.sleep(3)

            self.Actions.atualizar_ofertas()
        except:
            print("Problema Em Resetar Lista Ofertas.")

    def buscar_oferta(self, ofertas):
        try:
            for oferta in ofertas:
                match validar_oferta(oferta, self.filters):
                    case "OFERTA_VALIDA":
                        oferta["solicitar"]()
                        return
                    case "OFERTA_INVALIDA":
                        print("OFERTA INVALIDA!")

            self.Actions.scroll(scroll_value=-500)
        except:
            print("Problema Em Buscar Ofertas.")

    def solicitar_oferta(self):
        try:
            self.Actions.scroll(scroll_value=1500)

            if self.Actions.select_pedagio() == "INDISPONIVEL":
                self.atualizar_ofertas()
            else:
                self.Actions.scroll(scroll_value=-1500)
                self.Actions.select_data()
                self.Actions.solicitar_oferta()
        except:
            print("Problema Em Solicitar Oferta.")

    def confirmar_oferta(self):
        try:
            self.Actions.confirmar_oferta()
        except:
            print("Problema Em Confirmar Oferta.")

    def aprovar_oferta(self):
        try:
            self.Actions.scroll(scroll_value=500)
        except:
            print("Problema Em Aprovar Oferta.")

    def loop(self):
        while self.running:
            try:
                screen_state = self.StateMonitor.screen_state()["key"]

                match screen_state:
                    case "OFERTAS":
                        print("SCREEN: OFERTAS")

                        ofertas = self.get_ofertas()
                        lista_state = self.get_state_lista(ofertas=ofertas)

                        if lista_state in ["FINAL_DA_LISTA", "COMECO_DA_LISTA"]:
                            self.resetar_lista()

                        elif len(ofertas) < 1:
                            self.Actions.atualizar_ofertas()
                            continue

                        self.buscar_oferta(ofertas=ofertas)

                    case "DETALHE DA OFERTA":
                        print("SCREEN: DETALHE DA OFERTA")
                        self.solicitar_oferta()

                    case "CONFIRMAR SOLICITAÇÃO?":
                        print("SCREEN: CONFIRMAR SOLICITAÇÃO?")
                        self.confirmar_oferta()

                    case "AGUARDANDO APROVAÇÃO":
                        print("SCREEN: AGUARDANDO APROVAÇÃO")
                        self.aprovar_oferta()
                        
            except Exception as e:
                print(f"Erro no loop principal: {e}")

    def start(self):
        if not self.running:
            self.running = True
            self.thread_loop = threading.Thread(target=self.loop, daemon=True)
            self.AppiumDriver.start()
            self.thread_loop.start()
            print("Manager iniciado com sucesso!")

    def stop(self):
        if self.running:
            self.running = False
            self.thread_loop.join()
            self.AppiumDriver.stop()
            print("Manager encerrado com sucesso!")
