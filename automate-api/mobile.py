from appium import webdriver
from appium.options.android import UiAutomator2Options


class StradaLog:
    def __init__(self):
        options = UiAutomator2Options()                                                             # Inicializa instancia de configuração
        options.platform_name = "Android"                                                           # Definindo plataforma Android
        options.device_name = "emulator-5554"                                                       # Substitua pelo ID do dispositivo físico
        options.platform_version = "15.0"                                                           # Substitua pela versão correta do Android
        options.app = "C:/StradaLog.apk"                                                            # Caminho do APK
        options.automation_name = "UiAutomator2"                                                    # UIDriverAutomator
        options.no_reset = True                                                                     # Mantém o estado do app
        options.full_reset = False                                                                  # FullReset Falso
        
        self.driver = webdriver.Remote("http://192.168.3.250:4723", options=options)                # Conecta no webdriver do appium

    def select_element(self, xpath):
        try:
            # Localizar e elemento com xpath
            return self.driver.find_element("xpath", xpath)
        except Exception as e:
            print(f"Erro ao buscar elemento {xpath}: {str(e)}")
            return None
    
    def find_element(self, element, xpath):
        try:
            # Localizar e elemento com xpath
            return element.find_element("xpath", xpath)
        except Exception as e:
            print(f"Erro ao buscar elemento {xpath}: {str(e)}")
            return None

    def auto_scroll(self, mode="bottom", delay=500):
        # Obter dimensões da tela
        size = self.driver.get_window_size()

        # Obtendo tamanho da tela
        width = size["width"] / 2
        height = size["height"] / 2

        if mode == "bottom":
            end_height = height + (height / 2)

        elif mode == "top":
            end_height = height - (height / 2)

        # Simulando rolagem automatica
        self.driver.swipe(width, height, width, end_height, delay)

    def click(self, element):
        # Clicar no elemento
        element.click()

    def tap(self, x, y):
        self.driver.execute_script("mobile: tap", {"x": x, "y": y})