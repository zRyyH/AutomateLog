def status_lista(ofertas):
    for oferta in ofertas:
        try:
            bounds = oferta["oferta"].get_attribute("bounds")

            print("BOUNDS:", bounds)

            if bounds == "[21,1162][1059,1925]" or bounds == "[21,357][1059,1120]":
                return "COMECO_DA_LISTA"

            if bounds == "[21,1469][1059,2232]":
                return "FINAL_DA_LISTA"
        except:
            pass

    return "DESCONHECIDO"


def validar_oferta(oferta, filters):
    for filter in filters:
        produto = (
            filter["produto"].upper() == "INDIFERENTE"
            or oferta["produto"].upper() == filter["produto"].upper()
        )
        origem_1 = (
            filter["origem_1"].upper() == "INDIFERENTE"
            or oferta["origem_1"].upper() == filter["origem_1"].upper()
        )
        origem_2 = (
            filter["origem_2"].upper() == "INDIFERENTE"
            or oferta["origem_2"].upper() == filter["origem_2"].upper()
        )
        destino_1 = (
            filter["destino_1"].upper() == "INDIFERENTE"
            or oferta["destino_1"].upper() == filter["destino_1"].upper()
        )
        destino_2 = (
            filter["destino_2"].upper() == "INDIFERENTE"
            or oferta["destino_2"].upper() == filter["destino_2"].upper()
        )
        valor = int(oferta["valor"]) >= int(filter["valor_acima_de"])

        if produto and origem_1 and origem_2 and destino_1 and destino_2 and valor:
            return "OFERTA_VALIDA"
    return "OFERTA_INVALIDA"
