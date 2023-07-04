import pygame as pg
from tela_inicial import TelaInicial
from tela_inicial import TelaCreditos


def main():
    pg.init()

    # CONFIGURAÇÕES DAS TELAS
    info = pg.display.Info()
    largura_tela = info.current_w
    altura_tela = info.current_h
    tela = pg.display.set_mode((largura_tela, altura_tela))
    pg.display.set_caption("Tower Defense")

    tela_inicial = TelaInicial(largura_tela, altura_tela)
    tela_creditos = TelaCreditos(largura_tela, altura_tela)

    # JOGO ABERTO
    executando = True
    tela_atual = "inicial"  # tela_atual guarda a tela atual sendo exibida ("inicial" ou "creditos")
    while executando:
        # VERIFICAR OS CLIQUES NOS BOTÕES
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                executando = False
            elif evento.type == pg.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    mouse_pos = pg.mouse.get_pos()
                    if tela_atual == "inicial":
                        if tela_inicial.btn_jogar.collidepoint(mouse_pos):
                            tela_inicial.click_btn_jogar()
                        elif tela_inicial.btn_opcoes.collidepoint(mouse_pos):
                            tela_inicial.click_btn_opcoes()
                        elif tela_inicial.btn_creditos.collidepoint(mouse_pos):
                            tela_atual = "creditos"
                        elif tela_inicial.btn_sair.collidepoint(mouse_pos):
                            tela_inicial.click_btn_sair()
                            executando = False
                    elif tela_atual == "creditos":
                        if tela_creditos.botao_voltar.collidepoint(mouse_pos):
                            tela_atual = "inicial"

        if executando:
            if tela_atual == "inicial":
                # DESENHAR TELA INICIAL
                tela_inicial.desenhar_tela(tela)
            elif tela_atual == "creditos":
                # MOSTRAR TELA DE CRÉDITOS
                tela_creditos.mostrar_creditos(tela)

            pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()

