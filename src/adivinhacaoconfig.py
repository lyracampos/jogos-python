import random

class AdivinhacaoConfigs:
    
    def __init__(self, dificuldade):
        self.__dificuldade = dificuldade

    @property
    def dificuldade(self):
        return self.__dificuldade
    
    @dificuldade.setter
    def dificuldade(self, dificuldade):
        self.__dificuldade = dificuldade

    @property
    def numero_secreto(self):
        return random.randrange(1, 101)

    @property
    def numero_tentativas(self):
        return self.calcular_numero_tentativas()

    @property
    def pontos(self):
        return 100
        
    def calcular_numero_tentativas(self):
        if (self.__dificuldade == 1):
            return 20
        elif (self.__dificuldade == 2):
            return 10
        elif (self.__dificuldade == 3):
            return 5
        else:
            return 0

    def configuracoes_validas_para_iniciar(self):
        return self.__dificuldade >= 1 and self.__dificuldade <= 3