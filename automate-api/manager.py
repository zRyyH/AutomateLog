from services import validar_oferta, validar_bounds_refresh
from appium_driver import AppiumDriver
from state_monitor import StateMonitor
from actions import Actions

import traceback
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

    def atualizar_ofertas(self):
        try:
            while self.running:
                ofertas = self.StateMonitor.ofertas_state()

                match validar_bounds_refresh(ofertas):
                    case "COMECO_DA_LISTA":
                        self.Actions.scroll(scroll_value=500)
                        time.sleep(3)
                        self.Actions.scroll(scroll_value=-500)
                        print('COMECO DA LISTA')
                        return
                self.Actions.scroll(scroll_value=10000)
        except:
            print("Problema Em Atualizar Ofertas.")

    def buscar_oferta(self):
        try:
            while self.running:
                ofertas = self.StateMonitor.ofertas_state()

                for oferta in ofertas:
                    match validar_oferta(oferta, self.filters):
                        case "OFERTA_VALIDA":
                            oferta["solicitar"]()
                            return

                        case "FIM_DAS_OFERTAS":
                            self.atualizar_ofertas()
                            return
                        
                        case "COMECO_DA_LISTA":
                            self.atualizar_ofertas()
                            return
                        
                self.Actions.scroll(scroll_value=-500)
        except:
            print("Problema Em Buscar Ofertas.")
            traceback.print_exc()

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
            print("Problema Em Aprovar Oferta.")

    def aprovar_oferta(self):
        try:
            self.Actions.scroll(scroll_value=500)
        except:
            print("Problema Em Aprovar Oferta.")

    def loop(self):
        while self.running:
            try:
                screen_state = self.StateMonitor.screen_state()
                key = screen_state.get("key")

                if key == "OFERTAS":
                    print("SCREEN: OFERTAS")
                    self.buscar_oferta()

                elif key == "DETALHE DA OFERTA":
                    print("SCREEN: DETALHE DA OFERTA")
                    self.solicitar_oferta()

                elif key == "CONFIRMAR SOLICITAÇÃO?":
                    print("SCREEN: DETALHE DA OFERTA")
                    self.confirmar_oferta()

                elif key == "AGUARDANDO APROVAÇÃO":
                    print("SCREEN: DETALHE DA OFERTA")
                    self.aprovar_oferta()

                else:
                    print(f"SCREEN: {key} não reconhecida")

            except Exception as e:
                print(f"Erro no loop principal: {e}")
                traceback.print_exc()

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