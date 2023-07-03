import pygame as pg
from tela_inicial import TelaInicial


def main():
    pg.init()

    # CONFIGURAÇÕES DAS TELAS
    info = pg.display.Info()
    largura_tela = info.current_w
    altura_tela = info.current_h
    tela = pg.display.set_mode((largura_tela, altura_tela))
    pg.display.set_caption("Tower Defense")

    tela_inicial = TelaInicial(largura_tela, altura_tela)

    # JOGO ABERTO
    executando = True
    while executando:
        # VERIFICAR OS CLIQUES NOS BOTÕES EM TELA INICIAL
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                executando = False
            elif evento.type == pg.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    mouse_pos = pg.mouse.get_pos()
                    if tela_inicial.btn_jogar.collidepoint(mouse_pos):
                        tela_inicial.click_btn_jogar()
                    elif tela_inicial.btn_opcoes.collidepoint(mouse_pos):
                        tela_inicial.click_btn_opcoes()
                    elif tela_inicial.btn_creditos.collidepoint(mouse_pos):
                        tela_inicial.click_btn_creditos()
                    elif tela_inicial.btn_sair.collidepoint(mouse_pos):
                        tela_inicial.click_btn_sair()
                        executando = False

        if executando:
            # DESENHAR TELA INICIAL
            tela_inicial.desenhar_tela(tela)

            pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()