from mobile import StradaLog


XPATH_OFERTA_1 = "(//android.widget.FrameLayout[@resource-id='net.nuvem.mobile.carguero.release:id/cv_oferta'])[1]"
XPATH_OFERTA_2 = "(//android.widget.FrameLayout[@resource-id='net.nuvem.mobile.carguero.release:id/cv_oferta'])[2]"
XPATH_OFERTA_3 = "(//android.widget.FrameLayout[@resource-id='net.nuvem.mobile.carguero.release:id/cv_oferta'])[3]"
XPATH_PRODUTO = ("//*[@resource-id='net.nuvem.mobile.carguero.release:id/tv_produto_nome']")
XPATH_ORIGEM_1 = "//*[@resource-id='net.nuvem.mobile.carguero.release:id/tv_origem']"
XPATH_ORIGEM_2 = ("//*[@resource-id='net.nuvem.mobile.carguero.release:id/tv_local_coleta']")
XPATH_DESTINO_1 = "//*[@resource-id='net.nuvem.mobile.carguero.release:id/tv_destino']"
XPATH_DESTINO_2 = ("//*[@resource-id='net.nuvem.mobile.carguero.release:id/tv_local_descarga']")
XPATH_VALOR = "//*[@resource-id='net.nuvem.mobile.carguero.release:id/tv_valor']"
XPATH_SOLICITAR = ("//*[@resource-id='net.nuvem.mobile.carguero.release:id/btn_solicitar']")
XPATH_PEDAGIO = "//android.widget.Spinner[@resource-id='net.nuvem.mobile.carguero.release:id/spinner_field_adm']"
XPATH_CONFIRMAR_SOLICITAR = "//android.widget.Button[@resource-id='net.nuvem.mobile.carguero.release:id/fab_solicitar_oferta']"


AppAuto = StradaLog()


def refresh():
    AppAuto.auto_scroll(mode="bottom")
    
def check_ofertas():
    try:
        ofertas = []

        for xpath_oferta in [XPATH_OFERTA_1, XPATH_OFERTA_2]:
            oferta = AppAuto.select_element(xpath=xpath_oferta)

            produto = AppAuto.find_element(
                element=oferta, xpath=XPATH_PRODUTO
            ).text.upper()
            origem_1 = AppAuto.find_element(
                element=oferta, xpath=XPATH_ORIGEM_1
            ).text.upper()
            origem_2 = AppAuto.find_element(
                element=oferta, xpath=XPATH_ORIGEM_2
            ).text.upper()
            destino_1 = AppAuto.find_element(
                element=oferta, xpath=XPATH_DESTINO_1
            ).text.upper()
            destino_2 = AppAuto.find_element(
                element=oferta, xpath=XPATH_DESTINO_2
            ).text.upper()
            valor = AppAuto.find_element(element=oferta, xpath=XPATH_VALOR).text.upper()

            ofertas.append(
                {
                    "oferta": oferta,
                    "produto": produto,
                    "origem_1": origem_1,
                    "origem_2": origem_2,
                    "destino_1": destino_1,
                    "destino_2": destino_2,
                    "valor": valor,
                }
            )

        return ofertas
    except Exception as e:
        print(e)

def solicitar(element):
    btn = AppAuto.find_element(element=element, xpath=XPATH_SOLICITAR)
    btn.click()

def confirmar():
    try:
        btn = AppAuto.select_element(xpath=XPATH_PEDAGIO)
        btn.click()
        AppAuto.tap(x=800, y=1200)
    except:
        pass

    AppAuto.auto_scroll(mode="top", delay=100)
    btn = AppAuto.select_element(xpath=XPATH_CONFIRMAR_SOLICITAR)
    btn.click()

def rolagem():
    AppAuto.auto_scroll(mode='top')