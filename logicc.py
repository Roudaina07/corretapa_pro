import config

def calcular_descompte(subtotal, quantitat_persones, es_soci):
    if es_soci:
        return subtotal *  config.DESCOMPTE_SOCI
    elif quantitat_persones >=  config.MIN_PERSONES_GRUP:
        return subtotal * config.DESCOMPTE_GRUP
    return 0.0
def calcular_total_comanda(preu_tapa, quantitat_tapes, quantitat_persones, es_soci):
    subtotal_brut = preu_tapa * quantitat_tapes
    import_descompte = calcular_descompte(subtotal_brut, quantitat_persones, es_soci)
    base_imposable = subtotal_brut - import_descompte
    quota_iva = base_imposable * config.IVA_HOSTALERIA
    total_final = base_imposable + quota_iva
    return {
        "subtotal_brut": round(subtotal_brut, 2), "descompte": round(import_descompte, 2),
        "base_imposable": round(base_imposable, 2), "iva": round(quota_iva, 2), "total": round(total_final, 2)
    }