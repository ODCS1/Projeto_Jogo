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
    # MÉTODOS PARA DESENHAR OS ELEMENTOS NA TELA

    def desenhar_tela(self, tela):
        tela.blit(self.imagem_fundo, (0, 0))

        # chamando o método para desenhar os botões
        self.desenhar_botao(tela, self.btn_jogar, "JOGAR")
        self.desenhar_botao(tela, self.btn_opcoes, "OPÇÕES")
        self.desenhar_botao(tela, self.btn_creditos, "CRÉDITOS")
        self.desenhar_botao(tela, self.btn_sair, "SAIR")

    def desenhar_botao(self, tela, retangulo, texto):
        # botão em si
        pg.draw.rect(tela, self.COR_VERDE, retangulo, border_radius=10)

        # texto do botão
        texto_botao = self.fonte.render(texto, True, self.COR_BRANCA)
        posicao_texto_x = retangulo.x + (retangulo.width - texto_botao.get_width()) // 2
        posicao_texto_y = retangulo.y + (retangulo.height - texto_botao.get_height()) // 2
        tela.blit(texto_botao, (posicao_texto_x, posicao_texto_y))
    ##########################################################################################################


    ##########################################################################################################
    # MÉTODOS PARA OS BOTÕES

    def click_btn_jogar(self):
        print("Botão JOGAR clicado")

    def click_btn_opcoes(self):
        print("Botão OPÇÕES clicado")

    def click_btn_creditos(self):
        print("Botão CRÉDITOS clicado")

    def click_btn_sair(self):
        pg.quit()
    ##########################################################################################################