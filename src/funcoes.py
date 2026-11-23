def calcular_nota(candidato):
    """Calcula a nota ponderada do candidato."""
    nota = (
        candidato["habilidades"] * 0.45
        + candidato["determinacao"] * 0.40
        + candidato["experiencia"] * 0.15
    )
    return nota


def recomendar_ia(candidato):
    """Simula a IA, que considera principalmente a experiencia."""
    if candidato["experiencia"] >= 6:
        return "aprovar"
    return "rejeitar"


def verificar_decisao(candidato, decisao):
    """Compara a decisao do jogador com a classificacao do candidato."""
    nota = calcular_nota(candidato)
    adequado = nota >= 6.5

    if adequado and decisao == "aprovar":
        correta = True
    elif not adequado and decisao == "rejeitar":
        correta = True
    else:
        correta = False

    return correta, nota, adequado


def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)
