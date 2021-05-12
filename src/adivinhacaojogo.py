import random
from adivinhacaomenu import AdivinhacaoMenu
from adivinhacaoconfig import AdivinhacaoConfigs

class AdivinhacaoJogo:

    def __init__(self):
        menu = AdivinhacaoMenu()
        menu.exibir_menu_inicial()
        menu.exibir_menu_escolher_dificuldade()

        dificuldade  = menu.ler_dificuldade()
        config = AdivinhacaoConfigs(dificuldade)
        
        while not (config.configuracoes_validas_para_iniciar()):
            config.dificuldade = menu.ler_dificuldade_valida()

        menu.quebrar_linha()

        for tentativa in range(1, config.numero_tentativas + 1):
            menu.exibir_numero_tentativas_e_total_tentativas(tentativa, config.numero_tentativas)
            chute = menu.ler_chute()

            chute_invalido = chute < 1 or chute > 100
            chute_maior = chute > config.numero_secreto
            chute_menor = chute < config.numero_secreto

            if (chute_invalido):
                menu.exibir_digite_chute_valido()
                continue

            chute_certo = chute == config.numero_secreto
            if (chute_certo):
                menu.exibir_mensagem_parabens(config.pontos)
            else:
                if (chute_maior):
                    menu.exibir_mensagem_chute_maior()
                elif (chute_menor):
                    menu.exibir_mensagem_chute_menor()
            
                pontos_perdidos = abs(config.numero_secreto - chute)
                pontos = config.pontos - pontos_perdidos
            
            menu.quebrar_linha()
        menu.quebrar_linha()

        if (not chute_certo):
            menu.exibir_mensagem_nao_acertou(config.numero_secreto)

        menu.exibir_fim_do_jogo()


