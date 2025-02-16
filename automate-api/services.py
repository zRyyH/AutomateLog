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
        oferta_produto, filter_produto = (
            oferta["produto"].upper().strip(),
            filter["produto"].upper().strip(),
        )
        oferta_origem_1, filter_origem_1 = (
            oferta["origem_1"].upper().strip(),
            filter["origem_1"].upper().strip(),
        )
        oferta_origem_2, filter_origem_2 = (
            oferta["origem_2"].upper().strip(),
            filter["origem_2"].upper().strip(),
        )
        oferta_destino_1, filter_destino_1 = (
            oferta["destino_1"].upper().strip(),
            filter["destino_1"].upper().strip(),
        )
        oferta_destino_2, filter_destino_2 = (
            oferta["destino_2"].upper().strip(),
            filter["destino_2"].upper().strip(),
        )
        oferta_valor, filter_valor = int(oferta["valor"]), int(filter["valor_acima_de"])

        produto = filter_produto == "INDIFERENTE" or oferta_produto == filter_produto
        origem_1 = (
            filter_origem_1 == "INDIFERENTE" or oferta_origem_1 == filter_origem_1
        )
        origem_2 = (
            filter_origem_2 == "INDIFERENTE" or oferta_origem_2 == filter_origem_2
        )
        destino_1 = (
            filter_destino_1 == "INDIFERENTE" or oferta_destino_1 == filter_destino_1
        )
        destino_2 = (
            filter_destino_2 == "INDIFERENTE" or oferta_destino_2 == filter_destino_2
        )
        valor = oferta_valor >= filter_valor

        print(
            f"Produto: {produto}, Origem 1: {origem_1}, Origem 2: {origem_2}, Destino 1: {destino_1}, Destino 2: {destino_2}, Valor: {valor}"
        )

        print(
            f"Produto: {oferta_produto}, Origem 1: {oferta_origem_1}, Origem 2: {oferta_origem_2}, Destino 1: {oferta_destino_1}, Destino 2: {oferta_destino_2}, Valor: {oferta_valor}"
        )

        print(
            f"Produto: {filter_produto}, Origem 1: {filter_origem_1}, Origem 2: {filter_origem_2}, Destino 1: {filter_destino_1}, Destino 2: {filter_destino_2}, Valor: {filter_valor}"
        )

        if produto and origem_1 and origem_2 and destino_1 and destino_2 and valor:
            return "OFERTA_VALIDA"
    return "OFERTA_INVALIDA"
