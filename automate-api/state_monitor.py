from utils import load_json


class StateMonitor:
    def __init__(self, AppiumDriver):
        self.xpaths = load_json(path="xpaths.json")
        self.AppiumDriver = AppiumDriver

    def screen_state(self):
        for _, xpath in self.xpaths["navigation"].items():
            try:
                return {
                    "key": self.AppiumDriver.driver.find_element(
                        "xpath", xpath
                    ).text.upper()
                }
            except:
                pass
        return {}

    def ofertas_state(self):
        ofertas = []

        for _, xpath in self.xpaths["ofertas"].items():
            oferta = self.AppiumDriver.driver.find_element("xpath", xpath)

            try:
                produto = oferta.find_element(
                    "xpath", self.xpaths["oferta"]["xpath_produto"]
                ).text.upper()
                origem1 = oferta.find_element(
                    "xpath", self.xpaths["oferta"]["xpath_origem_1"]
                ).text.upper()
                origem2 = oferta.find_element(
                    "xpath", self.xpaths["oferta"]["xpath_origem_2"]
                ).text.upper()
                destino1 = oferta.find_element(
                    "xpath", self.xpaths["oferta"]["xpath_destino_1"]
                ).text.upper()
                destino2 = oferta.find_element(
                    "xpath", self.xpaths["oferta"]["xpath_destino_2"]
                ).text.upper()
                valor = oferta.find_element(
                    "xpath", self.xpaths["oferta"]["xpath_valor"]
                ).text.upper()

                data = {
                    "oferta": oferta,
                    "produto": produto,
                    "origem1": origem1,
                    "origem2": origem2,
                    "destino1": destino1,
                    "destino2": destino2,
                    "valor": valor,
                    "solicitar": oferta.click,
                }

                print(produto, origem1, destino1, valor)

                ofertas.append(data)

            except:
                pass
            
        return ofertas
