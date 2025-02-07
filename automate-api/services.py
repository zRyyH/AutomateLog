import traceback

def validar_oferta(oferta, filters):
    for filter in filters:
        valor = int(oferta["valor"].upper().split(',')[0].split(' ')[1])
        valor_minimo = int(filter["valor_acima_de"])

        isProduto = oferta["produto"].upper() == filter["produto"].upper() or filter["produto"].upper() == "INDIFERENTE"
        isOrigem1 = oferta["origem1"].upper() == filter["origem_1"].upper() or filter["origem_1"].upper() == "INDIFERENTE"
        isOrigem2 = oferta["origem2"].upper() == filter["origem_2"].upper() or filter["origem_2"].upper() == "INDIFERENTE"
        isDestino1 = oferta["destino1"].upper() == filter["destino_1"].upper() or filter["destino_1"].upper() == "INDIFERENTE"
        isDestino2 = oferta["destino2"].upper() == filter["destino_2"].upper() or filter["destino_2"].upper() == "INDIFERENTE"

        isValor = valor >= valor_minimo or valor_minimo == 0

        print(isProduto, isOrigem1, isOrigem2, isDestino1, isDestino2, isValor)

        if isProduto and isOrigem1 and isOrigem2 and isDestino1 and isDestino2 and isValor:
            return "OFERTA_VALIDA"

    if oferta["oferta"].get_attribute("bounds") == "[21,1469][1059,2232]":
        return "FIM_DAS_OFERTAS"

    if oferta["oferta"].get_attribute("bounds") == "[21,1162][1059,1925]":
        return "COMECO_DA_LISTA"


def validar_bounds_refresh(ofertas):
    for oferta in ofertas:
        try:
            if oferta["oferta"].get_attribute("bounds") == "[21,1162][1059,1925]":
                return "COMECO_DA_LISTA"
        except:
            traceback.print_exc()