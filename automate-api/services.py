def status_lista(ofertas):
    for oferta in ofertas:
        try:
            bounds = oferta["oferta"].get_attribute("bounds")

            print("BOUNDS:", bounds)

            if bounds == "[21,1162][1059,1925]" or bounds ==  "[21,357][1059,1120]":
                return "COMECO_DA_LISTA"
            
            if bounds == "[21,1469][1059,2232]":
                return "FINAL_DA_LISTA"
        except:
            pass

    return "DESCONHECIDO"


def validar_oferta(oferta, filters):
    for filter in filters:
        for key, value in filter.items():
            try:
                if oferta[key] != value and value != "INDIFERENTE":
                    return "OFERTA_INVALIDA"
            except:
                pass

        if int(oferta["valor"]) >= int(filter["valor_acima_de"]):
            return "OFERTA_VALIDA"