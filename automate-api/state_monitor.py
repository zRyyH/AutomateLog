from utils import load_json


class StateMonitor:
    def __init__(self, AppiumDriver):
        self.xpaths = load_json(path="xpaths.json")
        self.AppiumDriver = AppiumDriver

    def screen_state(self):
        for _, xpath in self.xpaths["navigation"].items():
            try:
                return {
                    "key": self.AppiumDriver.driver.find_element("xpath", xpath).text.upper()
                }
            except:
                pass
        return {}

    def ofertas_state(self):
        ofertas = []

        for key, xpath in self.xpaths["ofertas"].items():
            try:
                oferta = self.AppiumDriver.driver.find_element("xpath", xpath)

                xpath_oferta = self.xpaths["oferta"]
                produto = oferta.find_element(
                    "xpath", xpath_oferta["xpath_produto"]
                ).text.upper()
                origem_1 = oferta.find_element(
                    "xpath", xpath_oferta["xpath_origem_1"]
                ).text.upper()
                origem_2 = oferta.find_element(
                    "xpath", xpath_oferta["xpath_origem_2"]
                ).text.upper()

                ofertas.append(
                    {
                        "key": key,
                        "oferta": oferta,
                        "produto": produto,
                        "origem1": origem_1,
                        "origem2": origem_2,
                        "solicitar": oferta.click,
                    }
                )

            except:
                pass

        return ofertas
