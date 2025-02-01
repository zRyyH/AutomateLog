import traceback

def validar_oferta(oferta, filters):
    for filter in filters:
        isProduto = oferta["produto"].upper() == filter["produto"].upper()
        isOrigem1 = oferta["origem1"].upper() == filter["origem1"].upper()
        isOrigem2 = oferta["origem2"].upper() == filter["origem2"].upper()

        if isProduto and isOrigem1 and isOrigem2:
            print("OFERTA_VALIDA")
            return "OFERTA_VALIDA"
        
    if oferta["oferta"].get_attribute("bounds") == "[21,1469][1059,2232]":
        print("FIM_DAS_OFERTAS")
        return "FIM_DAS_OFERTAS"
    
def validar_bounds_refresh(ofertas):
    for oferta in ofertas:
        try:
            if oferta["oferta"].get_attribute("bounds") == "[21,1162][1059,1925]":
                print("COMECO_DA_LISTA")
                return "COMECO_DA_LISTA"
        except:
            traceback.print_exc()