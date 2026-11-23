import pygame

from src.config import LARGURA_TELA, ALTURA_TELA, FPS
from src.funcoes import (
    recomendar_ia,
    verificar_decisao,
)


CANDIDATOS = [
    {
        "nome": "Ana Souza",
        "experiencia": 8,
        "habilidades": 4,
        "determinacao": 5,
    },
    {
        "nome": "Bruno Lima",
        "experiencia": 3,
        "habilidades": 8,
        "determinacao": 8,
    },
    {
        "nome": "Carla Mendes",
        "experiencia": 7,
        "habilidades": 7,
        "determinacao": 7,
    },
    {
        "nome": "Diego Alves",
        "experiencia": 2,
        "habilidades": 6,
        "determinacao": 7,
    },
    {
        "nome": "Eva Santos",
        "experiencia": 6,
        "habilidades": 5,
        "determinacao": 8,
    },
]


def desenhar_texto(tela, fonte, texto, x, y, cor):
    """Desenha uma linha de texto na janela."""
    imagem = fonte.render(texto, True, cor)
    tela.blit(imagem, (x, y))


def desenhar_tela(tela, fonte, fonte_titulo, indice, decisao,
                  curriculos_analisados, decisoes_corretas):
    """Mostra o currículo atual e as instruções do jogo."""
    tela.fill((235, 235, 235))
    desenhar_texto(tela, fonte_titulo, "RecrutAI", 40, 30, (20, 20, 20))

    desenhar_texto(
        tela,
        fonte,
        f"Curriculos analisados: {curriculos_analisados}",
        40,
        95,
        (20, 20, 20),
    )
    desenhar_texto(
        tela,
        fonte,
        f"Decisoes corretas: {decisoes_corretas}",
        360,
        95,
        (20, 20, 20),
    )

    if indice >= len(CANDIDATOS):
        desenhar_texto(
            tela, fonte_titulo, "Avaliacao concluida!", 40, 200, (20, 20, 20)
        )
        desenhar_texto(
            tela, fonte, "Pressione ESC para fechar o jogo.", 40, 260, (20, 20, 20)
        )
        return

    candidato = CANDIDATOS[indice]
    recomendacao = recomendar_ia(candidato)
    texto_recomendacao = "APROVAR" if recomendacao == "aprovar" else "REJEITAR"

    desenhar_texto(
        tela, fonte, f"Curriculo {indice + 1} de {len(CANDIDATOS)}", 40, 155,
        (20, 20, 20),
    )
    desenhar_texto(tela, fonte, f"Candidato: {candidato['nome']}", 40, 205, (20, 20, 20))
    desenhar_texto(
        tela,
        fonte,
        f"Experiencia: {candidato['experiencia']}/10",
        40,
        255,
        (20, 20, 20),
    )
    desenhar_texto(
        tela,
        fonte,
        f"Habilidades tecnicas: {candidato['habilidades']}/10",
        40,
        295,
        (20, 20, 20),
    )
    desenhar_texto(
        tela,
        fonte,
        f"Determinacao: {candidato['determinacao']}/10",
        40,
        335,
        (20, 20, 20),
    )
    desenhar_texto(
        tela,
        fonte,
        f"Recomendacao da IA: {texto_recomendacao}",
        40,
        395,
        (20, 20, 20),
    )

    if decisao is None:
        desenhar_texto(
            tela, fonte, "A: aprovar     R: rejeitar", 40, 465, (20, 20, 20)
        )
    else:
        correta, nota, adequado = verificar_decisao(candidato, decisao)
        if correta:
            mensagem = f"Decisao correta! Nota: {nota:.1f}."
        else:
            mensagem = f"Decisao incorreta! Nota: {nota:.1f}."
        desenhar_texto(tela, fonte, mensagem, 40, 455, (20, 20, 20))
        if adequado:
            classificacao = "O candidato atende aos requisitos."
        else:
            classificacao = "O candidato nao atende aos requisitos."
        desenhar_texto(tela, fonte, classificacao, 40, 490, (20, 20, 20))
        desenhar_texto(
            tela, fonte, "ENTER: proximo curriculo", 40, 535, (20, 20, 20)
        )

    desenhar_texto(tela, fonte, "ESC: fechar o jogo", 560, 535, (20, 20, 20))


def executar_jogo():
    """Executa a avaliacao simples dos cinco curriculos."""
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("RecrutAI")
    relogio = pygame.time.Clock()
    fonte = pygame.font.Font(None, 30)
    fonte_titulo = pygame.font.Font(None, 48)

    rodando = True
    indice = 0
    decisao = None
    curriculos_analisados = 0
    decisoes_corretas = 0

    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
                elif indice < len(CANDIDATOS) and decisao is None:
                    if evento.key == pygame.K_a:
                        decisao = "aprovar"
                        curriculos_analisados += 1
                        correta, _, _ = verificar_decisao(
                            CANDIDATOS[indice], decisao
                        )
                        if correta:
                            decisoes_corretas += 1
                    elif evento.key == pygame.K_r:
                        decisao = "rejeitar"
                        curriculos_analisados += 1
                        correta, _, _ = verificar_decisao(
                            CANDIDATOS[indice], decisao
                        )
                        if correta:
                            decisoes_corretas += 1
                elif evento.key == pygame.K_RETURN and decisao is not None:
                    indice += 1
                    decisao = None

        desenhar_tela(
            tela,
            fonte,
            fonte_titulo,
            indice,
            decisao,
            curriculos_analisados,
            decisoes_corretas,
        )
        pygame.display.flip()

    pygame.quit()
