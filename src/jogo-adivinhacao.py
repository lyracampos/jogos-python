import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação.")
    print("*********************************")
    print("")

    print("escolha uma das dificuldades abaixo:")
    print("1 (fácil) 2 (médio) 3 (díficil)")

    dificuldade = int(input("digite: "))

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 100
    dificuldade_invalida = dificuldade < 1 or dificuldade > 3

    while (dificuldade_invalida):
        dificuldade = int(input("selecione uma dificuldade correta: "))
        dificuldade_invalida = dificuldade < 1 or dificuldade > 3

    if (dificuldade == 1):
        total_tentativas = 20
    elif (dificuldade == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    print("")

    for rodada in range(1, total_tentativas + 1):
        print("tentativa {} de {}".format(rodada, total_tentativas))
        chute = int(input("digite um número entre 1 e 100: "))

        if (chute < 1 or chute > 100):
            print("você precisa digitar um número entre 1 e 100.")
            continue

        acertou = chute == numero_secreto
        chutou_maior = chute > numero_secreto
        chutou_menor = chute < numero_secreto

        if (acertou):
            print("parabéns, você acertou! sua pontuação foi {}".format(pontos))
            break
        else:
            if (chutou_maior):
                print("você chutou maior, tente novamente.")
            elif (chutou_menor):
                print("você chutou um valor menor, tente novamente.")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        print("")

    print("")
    if (not acertou):
        print("Você não acertou, o número secreto é: {}".format(numero_secreto))

    print("fim de jogo!!!!")


if(__name__ == "__main__"):
    jogar()

