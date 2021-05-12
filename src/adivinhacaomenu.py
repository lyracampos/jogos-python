class AdivinhacaoMenu:

    def __init__(self):
        pass

    def exibir_menu_inicial(self):
        print("*********************************")
        print("Bem vindo ao jogo de adivinhação.")
        print("*********************************")
        print("")

    def exibir_menu_escolher_dificuldade(self):
        print("escolha uma das dificuldades abaixo:")
        print("1 (fácil) 2 (médio) 3 (díficil)")

    def exibir_numero_tentativas_e_total_tentativas(self, tentativa, numero_tentativas):
        print("tentativa {} de {}".format(tentativa, numero_tentativas))

    def exibir_mensagem_parabens(self, pontos):
         print("*********************************")
         print("parabéns, você acertou! sua pontuação foi {}".format(pontos))
         print("*********************************")
         print("")
    
    def exibir_mensagem_chute_maior(self):
        print("! - você chutou um número maior, tente novamente.")

    def exibir_mensagem_chute_menor(self):
        print("! - você chutou um número menor, tente novamente.")

    def exibir_mensagem_nao_acertou(self, numero_secreto):
         print("Você não acertou, o número secreto é: {}".format(numero_secreto))

    def exibir_fim_do_jogo(self):
        print("fim de jogo!!!!")

    def ler_dificuldade(self):
        return int(input("digite a dificuldade...: "))

    def ler_dificuldade_valida(self):
        return int(input("! - digite a dificuldade entre as opções válidas (1, 2, 3)...: "))

    def ler_chute(self):
        return int(input("digite um número entre 1 e 100...: "))

    def exibir_digite_chute_valido(self):
        print("! - o número digitado deve ser entre 1 e 100.")


    def quebrar_linha(self):
        print("")