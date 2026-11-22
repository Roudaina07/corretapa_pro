import config
import dades
import logica 
import interficie

def gestionar_aplicacio():
    interficie.mostrar_benvinguda()
    actiu = True
    while actiu:
        interficie.mostrar_menu_principal()
        opcio = interficie.demanar_opcio()
        if opcio == "1":
            bars= dades.obtenir_tots_els_bars()
            interficie.mostrar_carta_bars(bars)

        elif opcio == "2":
            zona = interficie.demanar_zona_cerca()
            trobats = dades_bars.filtrar_bars_per_zona(zona)
            if trobats:
                interficie.mostrar_carta_bars(trobats)
            else:
                interficie.mostrar_bar_no_trobat(zona)
        elif opcio == "3":
            reserva = interficie.demanar_dades_reserva()
            if reserva:
                bar =dades.cercar_bar_per_id(reserva["id_bar"])
                if not bar:
                    interficie.mostrar_bar_inexistent()
                elif not  dades.validar_disponibilitat(
                    bar["aforament_actual"], reserva["persones"], bar["aforament_max"]):
                    interficie.mostrar_error_aforament()
                else:
                    detall = logic.calcular_total_comanda(bar["preu_tapa"], reserva["tapes"], reserva["persones"], reserva["es_soci"])
                    dades.actualitzar_dades_bar(bar["id"], reserva["persones"], reserva["tapes"])
                    interficie.mostrar_resum_comanda(bar, reserva, detall)
        elif opcio == "4":
            stats = dades.calcular_estadistiques_globals(bars)
            interficie.mostrar_panell_estadistiques(stats)
        elif opcio == "0":
            interficie.mostrar_missatge_sortida()
            actiu = False
        else:
            interficie.mostrar_error_opcio_invalida()

if __name__ == "__main__":
    gestionar_aplicacio()