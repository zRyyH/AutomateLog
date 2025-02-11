from utils import load_json
import time


class StateMonitor:
    def __init__(self, AppiumDriver):
        self.xpaths = load_json(path="xpaths.json")
        self.AppiumDriver = AppiumDriver

    def screen_state(self):
        for _, xpath in self.xpaths["navigation"].items():
            try:
                t0 = time.time()

                element = self.AppiumDriver.driver.find_element(
                    "xpath", xpath
                ).text.upper()

                t1 = time.time()
                print("Demorou {}s para achar: {}".format(t1 - t0, _))
                return {"key": element}
            except:
                pass
        return {}

    def ofertas_state(self):
        ofertas = []

        t0 = time.time()

        for _, xpath in self.xpaths["ofertas"].items():
            try:
                oferta = self.AppiumDriver.driver.find_element("xpath", xpath)

                produto = oferta.find_element(
                    "xpath", self.xpaths["oferta"]["xpath_produto"]
                ).text
                origem1 = oferta.find_element(
                    "xpath", self.xpaths["oferta"]["xpath_origem_1"]
                ).text
                origem2 = oferta.find_element(
                    "xpath", self.xpaths["oferta"]["xpath_origem_2"]
                ).text
                destino1 = oferta.find_element(
                    "xpath", self.xpaths["oferta"]["xpath_destino_1"]
                ).text
                destino2 = oferta.find_element(
                    "xpath", self.xpaths["oferta"]["xpath_destino_2"]
                ).text
                valor = (
                    oferta.find_element("xpath", self.xpaths["oferta"]["xpath_valor"])
                    .text.split(",")[0]
                    .split(" ")[1]
                )

                data = {
                    "oferta": oferta,
                    "produto": str(produto.upper()),
                    "origem_1": str(origem1.upper()),
                    "origem_2": str(origem2.upper()),
                    "destino_1": str(destino1.upper()),
                    "destino_2": str(destino2.upper()),
                    "valor": int(valor),
                    "solicitar": oferta.click,
                }

                ofertas.append(data)
            except:
                pass

        t1 = time.time()
        print("Demorou {}s para achar as ofertas".format(t1 - t0))
        return ofertas
