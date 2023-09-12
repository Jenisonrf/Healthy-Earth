class Gerenciador:
    def __init__(self) -> None:
        self.dados = []  # Vai iniciar uma lista vazia para armazenar as análises de solo.

    def salvar_analise(self, analise): #Método para salvar uma análise de solo na lista de dados.
        self.dados.append(analise)  # Adiciona a análise à lista de dados.

    def mostrar_resultado(self): # Método para mostrar o resultado da análise mais recente na interface gráfica.
        resultado = self.obter_resultado()  # Obtém o resultado da análise mais recente.
                                            # Realiza ações na interface gráfica com base no resultado.
                                            
        if resultado == "resultado1":
            self.pages.setCurrentWidget(self.resultado1)
        elif resultado == "resultado2":
            self.pages.setCurrentWidget(self.resultado2)
        elif resultado == "resultado3":
            self.pages.setCurrentWidget(self.resultado3)
        elif resultado == "resultado4":
            self.pages.setCurrentWidget(self.resultado4)
        elif resultado == "resultado5":
            self.pages.setCurrentWidget(self.resultado5)
        elif resultado == "resultado6":
            self.pages.setCurrentWidget(self.resultado6)
        elif resultado == "resultado7":
            self.pages.setCurrentWidget(self.resultado7)
        elif resultado == "resultado8":
            self.pages.setCurrentWidget(self.resultado8)
        elif resultado == "resultado9":
            self.pages.setCurrentWidget(self.resultado9)
        elif resultado == "resultado10":
            self.pages.setCurrentWidget(self.resultado10)
        elif resultado == "resultado11":
            self.pages.setCurrentWidget(self.resultado11)
        elif resultado == "resultado12":
            self.pages.setCurrentWidget(self.resultado12)
        elif resultado == "resultado13":
            self.pages.setCurrentWidget(self.resultado13)
        elif resultado == "resultado14":
            self.pages.setCurrentWidget(self.resultado14)
        elif resultado == "resultado15":
            self.pages.setCurrentWidget(self.resultado15)
        elif resultado == "resultado16":
            self.pages.setCurrentWidget(self.resultado16)
        elif resultado == "resultado17":
            self.pages.setCurrentWidget(self.resultado17)
        elif resultado == "resultado18":
            self.pages.setCurrentWidget(self.resultado18)
