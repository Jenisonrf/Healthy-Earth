import sys

from model.analise_solo import Analise_Solo

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPixmap, QFont
from principal import Ui_MainWindow
from controle.gerenciador import Gerenciador
from PyQt6 import QtWidgets


from local.bancodedados import GerenciadorBancoDados

class Gui_cont (QMainWindow, Ui_MainWindow):
      
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.lista = []
        self.carregar_imagens()
        self.estilizar_botoes()  
        self.inicio.clicked.connect(self.mostrar_pagina_inicial)
        self.analise.clicked.connect(self.realizar_analise)
        self.contatos.clicked.connect(self.Contatos)
        self.sobre.clicked.connect(self.Sobre)
        self.proximo.clicked.connect(self.btn_proximo)
        self.voltar.clicked.connect(self.btn_voltar)
        self.configuracoes.clicked.connect(self.mostrar_pag_configuracao)
        self.usuarios_cadastrados.clicked.connect(self.mostrar_usarios_registrados)
        self.gerente = Gerenciador()

        self.frame_erro_login.hide()
        self.line_edit_login.setFocus()
        self.push_button_entrar.clicked.connect(self.realizar_login)
        self.pushButton_fechar_msg_login.clicked.connect(lambda : self.frame_erro_login.hide())

        self.proximo.clicked.connect(self.desmarcar_radio_botoes)        
        self.enviar.clicked.connect(self.exibir_resultado)
        
        self.criar_nova_conta.clicked.connect(self.passar_pag_criar_conta)

        self.bt_voltar.clicked.connect(self.voltar_a_pagina_de_inicio)
        self.sair.clicked.connect(self.voltar_a_pagina_de_inicio)
        self.historico.clicked.connect(self.pagina_historico)

        self.excluir_tudo.clicked.connect(self.limpar_lista)
        self.excluir.clicked.connect(self.excluir_linha_selecionada)
        self.registrar.clicked.connect(self.Criar_nova_conta)


        self.frame_22.hide()
        self.usuarios_cadastrados.hide()
        self.modo_adm.clicked.connect(self.visibilidade_usuarios)
        self.sair.clicked.connect(self.visibilidade_usuarios)
        self.deletar_conta.clicked.connect(self.mostrar_frame_deletar_conta)

        self.banco_de_dados = GerenciadorBancoDados('usuarios.db')

        self.msg_erro.hide() 
        self.fechar_msg_err.hide()
        self.fechar_msg_err.clicked.connect(self.fechar_mensagem_de_erro)
        self.sair.clicked.connect(self.mostrar_pagina_inicial)
        self.pushButton_fechar_msg_login.clicked.connect(self.mostrar_pagina_inicial)



    def mostrar_pagina_inicial(self):
        self.pages.setCurrentWidget(self.pag_inicial)

    def mostrar_frame_deletar_conta(self):
        if self.frame_22.isHidden():
            self.frame_22.show() 
        else:
            self.frame_22.hide()  # Oculta o frame

    def visibilidade_usuarios(self):
        if self.usuarios_cadastrados.isHidden():
            self.usuarios_cadastrados.show()  # Torna o botão visível
        else:
            self.usuarios_cadastrados.hide()  # Oculta o botão

    def fechar_mensagem_de_erro(self):
        self.msg_erro.hide()  # Oculte o frame de mensagem de erro quando o botão "Fechar mensagem de erro" for clicado
        self.fechar_msg_err.hide()

    def Criar_nova_conta(self):
        novo_login = self.line_edit_login_2.text()
        nova_senha = self.line_edit_senha_2.text()

        # Aqui vai vericar se todos os campos foram preenchidos
        if novo_login and nova_senha:
            #Adiciona um novo usuário ao banco de dados
            if self.banco_de_dados.adicionar_usuario(novo_login, nova_senha):
                print("Nova conta criada com sucesso!")
                # Limpa os campos após o registro bem-sucedido
                self.line_edit_login_2.clear()
                self.line_edit_senha_2.clear()
            else:
                print("Login já existe. Escolha outro login.")
        else:
            print("Preencha todos os campos.")
 
    def carregar_imagens(self):

        img_contatos = self.recalcular_tam_imagem('img/Contatos_img.png'
                                                , self.pag_inicial.width(),
                                              self.pag_inicial.height()
                                    )
        
        self.img_contatos.setPixmap(img_contatos)


        Img_logo = self.recalcular_tam_imagem('img/frame_fundo.png'
                                          , self.pag_inicial.width() * 1,
                                              self.pag_inicial.height() * 1
                                    )
        
        self.label_inicial.setPixmap(Img_logo)

        Img_copyrights = self.recalcular_tam_imagem('img/Copyright.png' 
                                                    , self.img_copyrigth.width() * 1, 
                                                        self.img_copyrigth.height() * 1)
        
        self.img_copyrigth.setPixmap(Img_copyrights)

        img_login = self.recalcular_tam_imagem('img/usuario.png'
                                               , self.label_icon_login.width() * 6,
                                                self.label_icon_login.height() * 6)
                                 
        
        self.label_icon_login.setPixmap(img_login)

    def estilizar_botoes(self):

        font = QFont()
        font.setBold(True)

 
        botoes = [self.inicio, self.analise, self.contatos, 
                  self.sobre, self.voltar, self.enviar, self.cinza,self.amarela, 
                  self.vermelha, self.argiloso, self.arenosa, self.baixa, self.media, 
                  self.alta, self.proximo, self.voltar, self.historico, self.sair, self.label_6,
                  self.registrar, self.criar_nova_conta, self.push_button_entrar, self.bt_voltar,
                  self.excluir, self.excluir_tudo, self.label_3, self.excluir_2, self.excluir_tudo_2, 
                  self.usuarios_cadastrados, self.configuracoes, self.sim, self.nao, self.deletar_conta, 
                  self.substituir, self.label_8, self.modo_adm]
        for botao in botoes:
            botao.setFont(font)
            botao.setStyleSheet("color: white;") 
    
    def mostrar_usarios_registrados (self):
        print("Botão 'Usuarios cadastrados' clicado. Mudando para a página 'Usuarios cadastrados'.")  
        self.pages.setCurrentWidget(self.page)  
    def passar_pag_criar_conta (self):

        print("Botão 'criar_nova_conta' clicado. Mudando para a página 'Criar Nova Conta'.")
        self.pag_login_e_sistema.setCurrentWidget(self.page_2)

    def excluir_linha_selecionada(self):
        selected_ranges = self.tableWidget_saida.selectedRanges()

        # Verifica se há pelo menos uma seleção
        if selected_ranges:
            # Obtém o índice da primeira linha selecionada
            row_index = selected_ranges[0].topRow()
            # Remove a linha da tabela
            self.tableWidget_saida.removeRow(row_index)
        print(self.lista)

    def limpar_lista(self):
        # Limpa a lista
        self.lista = []

        # Limpa a tabela
        self.tableWidget_saida.setRowCount(0)
  
    def pagina_historico(self):
        print("Botão 'Historico' clicado. Mudando para a página 'pagina de Historico'.")
        self.pages.setCurrentWidget (self.pag_historico)

    def voltar_a_pagina_de_inicio(self):
        self.pag_login_e_sistema.setCurrentWidget (self.pag_login)
    
    def mostrar_pag_configuracao(self):
        print("Botão 'Configuracao' clicado. Mudando para pagina de 'configuração'.")
        self.pages.setCurrentWidget(self.page_3)

    def mostrar_pagina_inicial(self):
        print("Botão 'inicio' clicado. Mudando para a página 'pagina_inicial'.")
        self.pages.setCurrentWidget(self.pag_inicial)

    def btn_voltar(self):
        self.pages.setCurrentWidget(self.pag_instrucoes)

    def btn_proximo(self):
        self.pages.setCurrentWidget(self.page_diagnostico)


    def realizar_analise(self):
        print("Botão 'realizar Análise' clicado. Mudando para a página 'análise'.")
        self.desmarcar_radio_botoes()  #Desmarcar os botões de radio
        self.pages.setCurrentWidget(self.pag_instrucoes)
            
    def Contatos(self):
        print("Botão 'Contatos' clicado. Mudando para a página 'Contatos'.")
        self.pages.setCurrentWidget(self.pag_contatos)

    def Sobre(self):
        print("Botão 'Sobre' clicado. Mudando para a página 'Sobre'.")
        self.pages.setCurrentWidget(self.pag_sobre)
    
    def desmarcar_radio_botoes(self):
        botoes_radio = [
            self.cinza, self.amarela, self.vermelha,
            self.argiloso, self.arenosa,
            self.baixa, self.media, self.alta
        ]
    
        for botao in botoes_radio:
             botao.setAutoExclusive(False)
             botao.setChecked(False)
             botao.setAutoExclusive(True)
             
             print(f"Desmarcando botão: {botao.text()}")

    def recalcular_tam_imagem(self, end_imagem: str, w: int = 16, h: int = 16):

        logo = QPixmap (end_imagem)
        logo = logo.scaled(w, h,
                            Qt.AspectRatioMode.KeepAspectRatio)
        return logo

    def exibir_resultado(self):
        textura = ""
        cor = ""
        umidade = ""

        if self.cinza.isChecked():
            cor = "Cinza"
        elif self.amarela.isChecked():
            cor = "Amarela"
        elif self.vermelha.isChecked():
            cor = "Vermelha"

        if self.argiloso.isChecked():
            textura = "Argilosa"
        elif self.arenosa.isChecked():
            textura = "Arenosa"

        if self.baixa.isChecked():
            umidade = "Baixa"
        elif self.media.isChecked():
            umidade = "Média"
        elif self.alta.isChecked():
            umidade = "Alta"

        if textura and cor and umidade and not self.msg_erro.isVisible():  # Verifica a visibilidade da mensagem de erro
            analise_solo = Analise_Solo(textura, cor, umidade)
            self.gerente.salvar_analise(analise_solo)
            self.mostrar_resultado(analise_solo.resultado)
            
            # Adicione as informações à tabela de histórico
            row_position = self.tableWidget_saida.rowCount()
            self.tableWidget_saida.insertRow(row_position)
            self.tableWidget_saida.setItem(row_position, 0, QtWidgets.QTableWidgetItem(textura))
            self.tableWidget_saida.setItem(row_position, 1, QtWidgets.QTableWidgetItem(cor))
            self.tableWidget_saida.setItem(row_position, 2, QtWidgets.QTableWidgetItem(umidade))
            
         
            self.msg_erro.hide()
        else:
            # Mostra uma mensagem de erro informando ao usuário o que está faltando
            self.msg_erro.show()
            self.fechar_msg_err.show()

    def mostrar_resultado(self, resultado): # Define a página de resultado com base no resultado fornecido
        if resultado == "resultado 1":
            self.pages.setCurrentWidget(self.resultado1)
        elif resultado == "resultado 2":
            self.pages.setCurrentWidget(self.resultado2)
        elif resultado == "resultado 3":
            self.pages.setCurrentWidget(self.resultado3)
        elif resultado == "resultado 4":
            self.pages.setCurrentWidget(self.resultado4)
        elif resultado == "resultado 5":
            self.pages.setCurrentWidget(self.resultado5)
        elif resultado == "resultado 6":
            self.pages.setCurrentWidget(self.resultado6)
        elif resultado == "resultado 7":
            self.pages.setCurrentWidget(self.resultado7)
        elif resultado == "resultado 8":
            self.pages.setCurrentWidget(self.resultado8)
        elif resultado == "resultado 9":
            self.pages.setCurrentWidget(self.resultado9)
        elif resultado == "resultado 10":
            self.pages.setCurrentWidget(self.resultado10)
        elif resultado == "resultado 11":
            self.pages.setCurrentWidget(self.resultado11)
        elif resultado == "resultado 12":
            self.pages.setCurrentWidget(self.resultado12)
        elif resultado == "resultado 13":
            self.pages.setCurrentWidget(self.resultado13)
        elif resultado == "resultado 14":
            self.pages.setCurrentWidget(self.resultado14)
        elif resultado == "resultado 15":
            self.pages.setCurrentWidget(self.resultado15)
        elif resultado == "resultado 16":
            self.pages.setCurrentWidget(self.resultado16)
        elif resultado == "resultado 17":
            self.pages.setCurrentWidget(self.resultado17)
        elif resultado == "resultado 18":
            self.pages.setCurrentWidget(self.resultado18)

    def realizar_login(self):
        '''Realizar o login do usuário'''
        login = self.line_edit_login.text()  # Recupera o texto do line edit
        senha = self.line_edit_senha.text()
        
        # Usa o GerenciadorBancoDados para verificar as credenciais
        if self.banco_de_dados.verificar_credenciais(login, senha):
            self.line_edit_login.setText('')
            self.line_edit_senha.setText('')
            self.frame_erro_login.hide()
            self.left_container.show()  # Mostrar o left_container
            self.pag_login_e_sistema.setCurrentWidget(self.pag_sistema)
        else:
            self.label_erro_login.setText('Seu login ou senha estão incorretos!')
            self.frame_erro_login.show()

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    view = Gui_cont()
    view.show()
    qt.exec()
