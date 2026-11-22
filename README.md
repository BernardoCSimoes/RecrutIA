# RecrutAI — Você confia na máquina?

Projeto final da disciplina de **Introdução a Algoritmos/Programação**, desenvolvido em **Python** com **Pygame**.

O **RecrutAI** é um jogo de análise de currículos que aborda o uso responsável da inteligência artificial em processos seletivos. O jogador assume o papel de um analista contratado para revisar decisões de uma IA que vem aprovando candidatos despreparados e rejeitando pessoas com potencial.

> **Status:** projeto em desenvolvimento. As regras abaixo descrevem a proposta planejada e poderão ser ajustadas ao longo da implementação.

## Integrantes

- **Nome:** Bernardo Coelho Simões

## Tema e proposta

O jogo explora os riscos de confiar cegamente em sistemas automatizados. A IA utilizada pela empresa dá peso excessivo à experiência profissional, o que pode produzir decisões injustas para vagas de estágio.

O jogador precisa avaliar as informações dos candidatos, comparar sua análise com a recomendação da IA e decidir se deve **aprovar** ou **rejeitar** cada currículo.

**Não será utilizada IA real:** as recomendações automatizadas serão simuladas por regras programadas em Python, como condicionais, listas, dicionários e funções.

## Objetivo do jogador

Analisar os currículos disponíveis, tomar decisões corretas e manter a confiança da empresa acima de **50%** até o fim da seleção.

Ao terminar todos os currículos sem ser demitido, o jogador conclui a partida com sucesso. Também será possível encerrar voluntariamente a sessão entre avaliações e visualizar o desempenho obtido.

## Como funciona o jogo

1. Um currículo é apresentado com nome fictício, vaga, experiência, habilidades e determinação.
2. Uma IA simulada apresenta sua recomendação de contratação.
3. O jogador decide **aprovar** ou **rejeitar** o candidato.
4. O jogo calcula se a decisão foi adequada e atualiza a pontuação e a confiança da empresa.
5. O jogador recebe um resumo da avaliação e escolhe continuar ou encerrar a sessão.

A avaliação dos candidatos utiliza uma **média ponderada**, com notas de 0 a 10:

| Critério | Peso |
| --- | ---: |
| Habilidades técnicas | 45% |
| Determinação | 40% |
| Experiência prática | 15% |

**Nota final:** `0.45 * habilidades + 0.40 * determinacao + 0.15 * experiencia`

No universo do jogo, candidatos com nota **maior ou igual a 6,5** são considerados adequados à vaga. Essa pontuação é uma regra fictícia da partida, não um método real de recrutamento.

## Regras e condições de encerramento

- A confiança da empresa começa em **80%**.
- Aprovar ou rejeitar corretamente um candidato aumenta a confiança em **3 pontos percentuais**.
- Aprovar um candidato inadequado reduz a confiança em **12 pontos percentuais**.
- Rejeitar um candidato adequado reduz a confiança em **8 pontos percentuais**.
- A confiança permanece entre **0% e 100%**.
- Ao chegar a **50% ou menos**, o jogador é demitido e a partida termina em derrota.
- Ao concluir os **15 currículos** previstos mantendo a confiança acima de 50%, o jogador vence.
- Entre currículos, o jogador pode sair voluntariamente e consultar seu desempenho.

## Pontuação e estatísticas

Ao final da sessão, o jogo deverá apresentar:

- Confiança final da empresa;
- Quantidade de currículos analisados;
- Quantidade de candidatos aprovados e rejeitados;
- Total de decisões corretas e incorretas;
- Taxa de acerto;
- Pontuação da partida.

## Controles previstos

A interação será feita por uma janela simples do Pygame, com textos e botões, utilizando mouse ou teclado conforme a implementação final.

- **A:** aprovar currículo;
- **R:** rejeitar currículo;
- **Enter:** avançar após visualizar o resultado da avaliação;
- **Esc:** solicitar saída entre avaliações.

Os controles poderão ser ajustados durante o desenvolvimento e serão atualizados neste README.

## Estrutura do projeto

O projeto utilizará o template oficial da disciplina e preservará sua organização básica:

- `main.py`: ponto de entrada do jogo;
- `src/`: lógica do jogo, interface e funções auxiliares;
- `assets/`: imagens, fontes e sons, se necessários;
- `data/`: dados dos currículos e informações persistentes, quando aplicável;
- `tests/`: testes da lógica do jogo com `pytest`;
- `docs/`: documentação, incluindo a proposta inicial.

## Como executar o projeto

É necessário ter o **Python** instalado.

1. Clone **seu próprio repositório** e abra a pasta do projeto:

   ```bash
   git clone https://github.com/BernardoCSimoes/RecrutAI.git
   cd RecrutAI
   ```

2. Instale as dependências:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Execute o jogo:

   ```bash
   python main.py
   ```

## Como executar os testes

Na pasta do projeto, execute:

```bash
python -m pytest
```

Os testes deverão verificar principalmente o cálculo da nota ponderada, a classificação dos candidatos, a atualização da confiança e as condições de encerramento.

## Organização das entregas

- **Entrega 1:** definição do jogo e documentação em `docs/proposta.md` (prazo original: 15/11/2026);
- **Entrega 2:** versão parcial executável com janela Pygame, exibição de currículo e decisões básicas (22/11/2026);
- **Entrega 3:** jogo completo, documentação e testes (29/11/2026);
- **Apresentação:** semana de 30/11/2026.

## Originalidade e recursos externos

O RecrutAI é uma proposta de jogo autoral desenvolvida para a disciplina. A simulação da IA e os critérios de avaliação dos currículos são fictícios e têm finalidade educativa.

O projeto parte do [template oficial de Introdução a Algoritmos da PUC Minas](https://github.com/ICEI-PUC-Minas-PPL-CDIA/IntroAlgs_pygame_template). Recursos adicionais utilizados durante o desenvolvimento, caso existam, serão identificados aqui com sua origem e licença, quando disponível.

