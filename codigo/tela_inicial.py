import pygame as pg
import os


class TelaInicial:
    def __init__(self, largura, altura):
        self.largura_tela = largura
        self.altura_tela = altura

        ##########################################################################################################
        # IMAGEM DE FUNDO DA TELA INICIAL
        caminho_imagem_fundo = os.path.join("assets", "imagens", "fundo", "fundo-inicial.png")
        self.imagem_fundo = pg.image.load(caminho_imagem_fundo)
        self.imagem_fundo = pg.transform.scale(self.imagem_fundo, (self.largura_tela, self.altura_tela))
        ##########################################################################################################

        ##########################################################################################################
        # DEFINIR CONFIGURAÇÕES DE ESTILO
        self.COR_BRANCA = (255, 255, 255)
        self.COR_VERDE = (0, 255, 0)
        self.fonte = pg.font.Font(None, 24)
        ##########################################################################################################

        ##########################################################################################################
        # CONFIGURAÇÃO DOS BOTÕES
        self.largura_botao = 200
        self.altura_botao = 50
        self.espaco_entre_botoes = 20

        self.posicao_x_primeiro_botao = (self.largura_tela - self.largura_botao) // 2
        self.posicao_y_primeiro_botao = (self.altura_tela - self.altura_botao * 4 - self.espaco_entre_botoes * 3) // 2
        ##########################################################################################################

        ##########################################################################################################
        # CRIAÇÃO DOS BOTÕES
        self.btn_jogar = pg.Rect(self.posicao_x_primeiro_botao, self.posicao_y_primeiro_botao, self.largura_botao, self.altura_botao)
        self.btn_opcoes = pg.Rect(self.posicao_x_primeiro_botao, self.posicao_y_primeiro_botao + self.altura_botao + self.espaco_entre_botoes, self.largura_botao, self.altura_botao)
        self.btn_creditos = pg.Rect(self.posicao_x_primeiro_botao, self.posicao_y_primeiro_botao + (self.altura_botao + self.espaco_entre_botoes) * 2, self.largura_botao, self.altura_botao)
        self.btn_sair = pg.Rect(self.posicao_x_primeiro_botao, self.posicao_y_primeiro_botao + (self.altura_botao + self.espaco_entre_botoes) * 3, self.largura_botao, self.altura_botao)
        ##########################################################################################################

        ##########################################################################################################
        # Tela de créditos
        self.tela_creditos = TelaCreditos(self.largura_tela, self.altura_tela)
        ##########################################################################################################

    ##########################################################################################################
    # MÉTODOS PARA DESENHAR OS ELEMENTOS NA TELA

    def desenhar_tela(self, tela):
        tela.blit(self.imagem_fundo, (0, 0))

        # chamando o método para desenhar os botões
        self.desenhar_botao(tela, self.btn_jogar, "JOGAR")
        self.desenhar_botao(tela, self.btn_opcoes, "OPÇÕES")
        self.desenhar_botao(tela, self.btn_creditos, "CRÉDITOS")
        self.desenhar_botao(tela, self.btn_sair, "SAIR")

    def desenhar_botao(self, tela, retangulo, texto):
        mouse_pos = pg.mouse.get_pos()
        if retangulo.collidepoint(mouse_pos):
            cor_botao = (100, 100, 100)
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
        else:
            cor_botao = (0, 255, 0)
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)

        # Desenha o botão
        pg.draw.rect(tela, cor_botao, retangulo, border_radius=10)

        # texto do botão
        texto_botao = self.fonte.render(texto, True, self.COR_BRANCA)
        posicao_texto_x = retangulo.x + (retangulo.width - texto_botao.get_width()) // 2
        posicao_texto_y = retangulo.y + (retangulo.height - texto_botao.get_height()) // 2
        tela.blit(texto_botao, (posicao_texto_x, posicao_texto_y))

    def processar_eventos(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return True

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clique do botão esquerdo do mouse
                    mouse_pos = pg.mouse.get_pos()
                    if self.btn_jogar.collidepoint(mouse_pos):
                        self.click_btn_jogar()
                    elif self.btn_opcoes.collidepoint(mouse_pos):
                        self.click_btn_opcoes()
                    elif self.btn_creditos.collidepoint(mouse_pos):
                        self.click_btn_creditos()
                    elif self.btn_sair.collidepoint(mouse_pos):
                        self.click_btn_sair()

        return False


class TelaCreditos:
    def __init__(self, largura, altura):
        self.largura_tela = largura
        self.altura_tela = altura

        # Definir configurações de estilo
        self.COR_BRANCA = (255, 255, 255)
        self.fonte = pg.font.Font(None, 24)

        # Configurar botão de voltar
        self.largura_botao_voltar = 200
        self.altura_botao_voltar = 50
        self.posicao_x_botao_voltar = (self.largura_tela - self.largura_botao_voltar) // 2
        self.posicao_y_botao_voltar = self.altura_tela - self.altura_botao_voltar - 20
        self.botao_voltar = pg.Rect(self.posicao_x_botao_voltar, self.posicao_y_botao_voltar,
                                    self.largura_botao_voltar, self.altura_botao_voltar)

    def mostrar_creditos(self, tela):
        tela.fill((0, 0, 0))  # Preenche a tela com preto

        # Desenhar texto de créditos
        texto1 = self.fonte.render("Criadores:", True, self.COR_BRANCA)
        texto2 = self.fonte.render("- Antonio", True, self.COR_BRANCA)
        texto3 = self.fonte.render("- Digas", True, self.COR_BRANCA)
        texto4 = self.fonte.render("- Vitor", True, self.COR_BRANCA)
        texto5 = self.fonte.render("Agradecimentos:" ,True, self.COR_BRANCA)
        texto6 = self.fonte.render("- Andreia", True, self.COR_BRANCA)
        texto7 = self.fonte.render("- Maligno", True, self.COR_BRANCA)
        posicao_texto1 = (self.largura_tela - texto1.get_width()) // 2
        posicao_texto2 = (self.largura_tela - texto2.get_width()) // 2
        posicao_texto3 = (self.largura_tela - texto3.get_width()) // 2
        posicao_texto4 = (self.largura_tela - texto4.get_width()) // 2
        posicao_texto5 = (self.largura_tela - texto4.get_width()) // 2
        posicao_texto6 = (self.largura_tela - texto4.get_width()) // 2
        posicao_texto7 = (self.largura_tela - texto4.get_width()) // 2
        tela.blit(texto1, (posicao_texto1, 100))
        tela.blit(texto2, (posicao_texto2, 150))
        tela.blit(texto3, (posicao_texto3, 200))
        tela.blit(texto4, (posicao_texto4, 250))
        tela.blit(texto4, (posicao_texto4, 250))
        tela.blit(texto5, (posicao_texto5, 350))
        tela.blit(texto6, (posicao_texto4, 400))
        tela.blit(texto7, (posicao_texto5, 450))
        # Desenhar botão de voltar
        pg.draw.rect(tela, (0, 255, 0), self.botao_voltar, border_radius=10)
        texto_botao = self.fonte.render("Voltar", True, self.COR_BRANCA)
        posicao_texto_x = self.posicao_x_botao_voltar + (self.largura_botao_voltar - texto_botao.get_width()) // 2
        posicao_texto_y = self.posicao_y_botao_voltar + (self.altura_botao_voltar - texto_botao.get_height()) // 2
        tela.blit(texto_botao, (posicao_texto_x, posicao_texto_y))


    ##########################################################################################################
    # MÉTODOS PARA OS BOTÕES

    def click_btn_jogar(self):
        print("Botão JOGAR clicado")

    def click_btn_opcoes(self):
        print("Botão OPÇÕES clicado")

    def click_btn_creditos(self):
        self.mostrar_creditos()

    def click_btn_sair(self):
        pg.quit()
    ##########################################################################################################
