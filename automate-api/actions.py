from selenium.webdriver.common.action_chains import ActionChains
from cloud_vision import position_sem_parar
from utils import load_json
import time


class Actions:
    def __init__(self, AppiumDriver):
        self.xpaths = load_json(path="xpaths.json")
        self.AppiumDriver = AppiumDriver

    def scroll(self, scroll_value):
        actions = ActionChains(self.AppiumDriver.driver)
        actions.w3c_actions.pointer_action.move_to_location(100, 1000)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(100, 1000 + scroll_value)
        actions.w3c_actions.pointer_action.pointer_up()
        actions.perform()

    def click(self, x, y):
        actions = ActionChains(self.AppiumDriver.driver)
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pointer_up()
        actions.perform()

    def atualizar_ofertas(self):
        print("ATUALIZANDO OFERTAS")
        self.scroll(scroll_value=250)
        time.sleep(3)

    def select_pedagio(self):
        try:
            time.sleep(0.5)
            self.AppiumDriver.driver.find_element(
                "xpath", self.xpaths["detalhe_da_oferta"]["xpath_pedagio"]
            ).click()

            time.sleep(0.5)
            self.AppiumDriver.driver.save_screenshot("screenshot.png")
            time.sleep(0.5)

            position = position_sem_parar()

            if position:
                self.click(**position)
                return "DISPONIVEL"
            else:
                self.AppiumDriver.driver.find_element(
                    "xpath", self.xpaths["detalhe_da_oferta"]["back_screen"]
                ).click()
                return "INDISPONIVEL"
        except:
            return "PADRAO"

    def select_data(self):
        try:
            self.AppiumDriver.driver.find_element(
                "xpath", self.xpaths["detalhe_da_oferta"]["xpath_data_1"]
            ).click()

            return True
        except:
            return False

    def solicitar_oferta(self):
        try:
            self.AppiumDriver.driver.find_element(
                "xpath", self.xpaths["detalhe_da_oferta"]["xpath_solicitar"]
            ).click()

            return True
        except:
            return False

    def confirmar_oferta(self):
        try:
            ##### CUIDADO ESSE COMANDO CONFIRMA A OFERTA #####
            self.AppiumDriver.driver.find_element(
                "xpath", self.xpaths["detalhe_da_oferta"]["cancelar"]
            ).click()

            print("=== ORDEM CONFIRMADA ===")

            return True
        except:
            return False
