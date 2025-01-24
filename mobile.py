from appium import webdriver
from appium.options.android import UiAutomator2Options


class StradaLog:
    def __init__(self):
        # Configuração do dispositivo usando AppiumOptions
        options = UiAutomator2Options()  # Inicializa instancia de configuração

        options.platform_name = "Android"  # Definindo plataforma Android
        options.device_name = "emulator-5554"  # Substitua pelo ID do dispositivo físico
        options.platform_version = "15.0"  # Substitua pela versão correta do Android
        options.app = "C:/Users/zryyh/Downloads/StradaLog.apk"  # Caminho do APK
        options.automation_name = "UiAutomator2"  #
        options.no_reset = True  # Mantém o estado do app
        options.full_reset = False

        # Inicializa a sessão do Appium
        self.driver = webdriver.Remote("http://localhost:4723", options=options)

    def select_element(self, xpath):
        try:
            # Localizar e elemento com xpath
            return self.driver.find_element("xpath", xpath)
        except:
            raise Exception(f"Elemento: {xpath} não encontrado!")

    def find_element(self, element, xpath):
        try:
            # Localizar e elemento com xpath
            return element.find_element("xpath", xpath)
        except:
            raise Exception(f"Elemento: {xpath} não encontrado!")

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