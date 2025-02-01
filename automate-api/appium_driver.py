from appium import webdriver
from appium.options.android import UiAutomator2Options


class AppiumDriver:
    def __init__(self):
        # Configuração inicial das opções para o Appium
        self.options = UiAutomator2Options()

        # Definindo a plataforma Android
        self.options.platform_name = "Android"

        # Nome ou ID do dispositivo (pode ser um emulador ou dispositivo físico)
        self.options.device_name = "emulator-5554"

        # Versão do Android no dispositivo
        self.options.platform_version = "10.0"

        # Caminho do arquivo APK a ser instalado/executado
        self.options.app = "C:/StradaLog.apk"

        # Nome do motor de automação usado pelo Appium
        self.options.automation_name = "UiAutomator2"

        # Define que o estado do app (dados, cache) não será reiniciado
        self.options.no_reset = True

        # Define que não será feito um reset completo do app antes da execução
        self.options.full_reset = False

        # Inicializa o atributo do driver como None, ele será atribuído ao iniciar
        self.driver = None

    def start(self):
        try:
            # Cria a conexão remota com o servidor Appium, passando as opções configuradas
            self.driver = webdriver.Remote(
                f"http://127.0.0.1:4723", options=self.options
            )

            # Mensagem de sucesso
            print("Driver iniciado com sucesso.")

        except Exception as e:
            # Captura e exibe qualquer erro ocorrido durante a execução
            print(f"Erro ao iniciar o driver: {e}")

    def stop(self):
        if self.driver:
            print("Encerrando o driver...")
            try:
                # Finaliza a conexão com o servidor Appium e encerra o driver
                self.driver.quit()
            except Exception as e:
                # Captura e exibe qualquer erro ocorrido durante o encerramento
                print(f"Erro ao encerrar o driver: {e}")
            finally:
                # Garante que o atributo `driver` seja definido como None após o encerramento
                self.driver = None
