class Analise_Solo:
    def __init__(self, textura, cor, umidade):
        # Inicializa os atributos da instância com os valores fornecidos.
        self.textura = textura
        self.cor = cor
        self.umidade = umidade
        self.resultado = ''

    @property
    def resultado(self):
        # Propriedade que retorna o resultado da análise.
        return self.__resultado
    
    @resultado.setter
    # Define o resultado da análise com base nos valores de textura, cor e umidade.
    def resultado(self, resultado):
        if self.textura == "Arenosa" and self.cor == "Cinza" and self.umidade == "Baixa":
            self.__resultado = "resultado 1"

        elif self.textura == "Argilosa" and self.cor == "Vermelha" and self.umidade == "Média":
            self.__resultado = "resultado 2"

        elif self.textura == "Arenosa" and self.cor == "Amarela" and self.umidade == "Alta":
            self.__resultado = "resultado 3"

        elif self.textura == "Argilosa" and self.cor == "Amarela" and self.umidade == "Baixa":
            self.__resultado = "resultado 4"

        elif self.textura == "Argilosa" and self.cor == "Amarela" and self.umidade == "Alta":
            self.__resultado = "resultado 5"

        elif self.textura == "Arenosa" and self.cor == "Vermelha" and self.umidade == "Média":
            self.__resultado = "resultado 6"

        elif self.textura == "Argilosa" and self.cor == "Vermelha" and self.umidade == "Alta":
            self.__resultado = "resultado 7"

        elif self.textura == "Arenosa" and self.cor == "Cinza" and self.umidade == "Alta":
            self.__resultado = "resultado 8"

        elif self.textura == "Argilosa" and self.cor == "Cinza" and self.umidade == "Baixa":
            self.__resultado = "resultado 9"

        elif self.textura == "Argilosa" and self.cor == "Cinza" and self.umidade == "Alta":
            self.__resultado = "resultado 10"

        elif self.textura == "Arenosa" and self.cor == "Cinza" and self.umidade == "Média":
            self.__resultado = "resultado 11"

        elif self.textura == "Arenosa" and self.cor == "Vermelha" and self.umidade == "Baixa":
            self.__resultado = "resultado 12"

        elif self.textura == "Arenosa" and self.cor == "Vermelha" and self.umidade == "Alta":
            self.__resultado = "resultado 13"

        elif self.textura == "Arenosa" and self.cor == "Amarela" and self.umidade == "Baixa":
            self.__resultado = "resultado 14"

        elif self.textura == "Arenosa" and self.cor == "Amarela" and self.umidade == "Média":
            self.__resultado = "resultado 15"

        elif self.textura == "Argilosa" and self.cor == "Cinza" and self.umidade == "Média":
            self.__resultado = "resultado 16"

        elif self.textura == "Argilosa" and self.cor == "Vermelha" and self.umidade == "Baixa":
            self.__resultado = "resultado 17"

        elif self.textura == "Argilosa" and self.cor == "Amarela" and self.umidade == "Média":
            self.__resultado = "resultado 18"

    @property
    def textura(self):
        # Propriedade que retorna a textura do solo.
        return self.__textura
    
    @textura.setter
    def textura(self, value):
        # Define a textura do solo, aceitando apenas "Arenosa" ou "Argilosa".
        if value in ["Arenosa", "Argilosa"]:
            self.__textura = value
        else:
            print("Valor inválido para textura")

    @property
    def cor(self):
        # Propriedade que retorna a cor do solo.
        return self.__cor
    
    @cor.setter
    def cor(self, value):
        # Define a cor do solo, aceitando apenas "Cinza", "Vermelha" ou "Amarela".
        if value in ["Cinza", "Vermelha", "Amarela"]:
            self.__cor = value
        else:
            print("Valor inválido para cor")

    @property
    def umidade(self):
        # Propriedade que retorna a umidade do solo.
        return self.__umidade
    
    @umidade.setter
    def umidade(self, value):
        # Define a umidade do solo, aceitando apenas "Baixa", "Média" ou "Alta".
        if value in ["Baixa", "Média", "Alta"]:
            self.__umidade = value
        else:
            print("Valor inválido para umidade")