# Proposta Inicial do Jogo

## 1. Nome provisório do jogo

**Nome:** RecrutIA — Você confia na máquina?

## 2. Integrantes do grupo

- Nome 1: **Bernardo Coelho Simões**

## 3. Tema escolhido

**Tema:** Inteligência Artificial no Cotidiano — confiabilidade de sistemas inteligentes, vieses em decisões automatizadas e importância da supervisão humana.

**Como esse tema se relaciona com o jogo?** A empresa fictícia utiliza uma IA para avaliar candidatos a estágio, mas suas recomendações nem sempre são adequadas. O jogador revisa cada currículo e decide se aprova ou rejeita o candidato. As decisões demonstram os riscos de confiar cegamente em sistemas automatizados e a importância de verificar seus critérios.

## 4. Tipo de jogo

**Tipo escolhido:** Simulação simples de tomada de decisões e análise de currículos, com pontuação, reputação e avaliações em sequência.

## 5. Descrição geral do jogo

**Descrição:** Em uma empresa de tecnologia, uma IA passou a selecionar estagiários automaticamente, mas começou a rejeitar pessoas qualificadas e aprovar outras despreparadas. O jogador assume o papel de analista contratado para revisar as recomendações da IA. Em cada rodada, a tela apresenta um candidato fictício, a vaga, indicadores de experiência, habilidades e determinação, além do parecer da IA. O jogador escolhe aprovar ou rejeitar o currículo. Após a escolha, recebe um retorno sobre a decisão e pode avaliar o próximo candidato ou encerrar a partida. A interface será simples, feita em Python com Pygame, usando principalmente textos, botões e uma barra de confiança da empresa.

## 6. Objetivo do jogador

**Objetivo:** Tomar decisões adequadas sobre os currículos, corrigir possíveis erros da IA, acumular pontos e manter a confiança da empresa acima de 50%. A meta de conclusão será analisar todos os currículos previstos para a partida sem ser desligado.

## 7. Regras principais

- **Regra 1:** O jogador começa com **80% de confiança da empresa**. Cada rodada apresenta um currículo e uma recomendação da IA, que pode estar correta ou incorreta.
- **Regra 2:** Cada candidato recebe três notas de **0 a 10**: experiência (E), habilidades (H) e determinação (D). A adequação à vaga é calculada por **nota = 0,15 × E + 0,45 × H + 0,40 × D**. Candidatos com nota **maior ou igual a 6,5** são considerados adequados às vagas fictícias do jogo. A nota final fica oculta até a decisão do jogador.
- **Regra 3:** A IA é **simulada por regras simples**, sem modelo real, e valoriza excessivamente a experiência. Por isso, pode recomendar decisões diferentes da avaliação definida pelo jogo. O jogador deve analisar os três indicadores antes de decidir.
- **Regra 4:** Decisões corretas rendem **10 pontos** e aumentam a confiança em **3 pontos percentuais**. Aprovar alguém inadequado reduz a confiança em **12 pontos percentuais**; rejeitar alguém adequado reduz em **8 pontos percentuais**. Decisões incorretas não rendem pontos. A confiança fica limitada ao intervalo entre 0% e 100%.
- **Regra 5:** Após cada decisão, o resultado é mostrado e o jogador pode prosseguir ou sair. Se a confiança chegar a **50% ou menos**, a partida termina automaticamente com derrota. As estatísticas são exibidas ao final.

## 8. Condição de vitória

**Condição de vitória:** Concluir a avaliação de todos os **15 currículos fictícios previstos inicialmente**, mantendo a confiança da empresa **acima de 50%**. A tela final mostrará os resultados da partida. O jogador também poderá sair antes de concluir todas as avaliações, mas isso será tratado como encerramento voluntário, não como vitória.

## 9. Condição de derrota ou encerramento

**Condição de derrota ou encerramento:** O jogador perde quando a confiança da empresa chega a **50% ou menos**. Nesse caso, o jogo informa que a empresa decidiu desligá-lo por considerar que seu trabalho não apresentou melhorias e que a IA pode substituí-lo. A partida também pode terminar voluntariamente, após a conclusão de um currículo, ou ser concluída quando todos os currículos forem avaliados. Em qualquer encerramento, serão exibidas estatísticas como currículos analisados, aprovados, rejeitados, acertos, erros, taxa de acerto, pontuação e confiança final.

## 10. Elementos previstos no jogo

- **Personagem ou elemento principal:** O próprio jogador, no papel de analista de recrutamento, representado por suas decisões na interface.
- **Obstáculos ou desafios:** Recomendações equivocadas da IA, candidatos com perfis diferentes e risco de perder a confiança da empresa.
- **Itens ou objetos de interação (se houver):** Currículos fictícios, dados dos candidatos, pareceres da IA e botões para aprovar, rejeitar, continuar ou encerrar.
- **Pontuação, vidas, tempo ou progresso:** Pontos por decisões corretas, confiança percentual da empresa, quantidade de currículos avaliados e estatísticas de acerto.

## 11. Controles previstos

**Controles:** O jogador poderá usar o **mouse** para selecionar os botões da interface. Também estão previstos os atalhos **A** (aprovar) e **R** (rejeitar) durante a análise, **Enter** (próximo currículo) e **Esc** (encerrar após finalizar uma avaliação). Os comandos serão exibidos na tela.

## 12. Principais dificuldades esperadas

- **Dificuldade 1:** Aprender a apresentar textos e botões e reconhecer cliques ou teclas usando Pygame.
- **Dificuldade 2:** Organizar as funções de cálculo, recomendações da IA, pontuação e confiança sem misturá-las com a interface.
- **Dificuldade 3:** Testar os diferentes resultados possíveis, incluindo contratações inadequadas, rejeições incorretas, vitória, derrota e saída voluntária.

## 13. Escopo mínimo para a entrega final

**Escopo mínimo:** Um jogo executável com uma janela Pygame simples, **15 currículos fictícios** definidos em listas e dicionários, exibição de informações e parecer da IA, botões ou atalhos para aprovar/rejeitar, cálculo da adequação por média ponderada, atualização da pontuação e da confiança, condição de derrota em 50%, conclusão após todos os currículos, opção de saída após cada avaliação e tela final com estatísticas. O código será dividido em funções e módulos simples, com `README.md`, esta proposta e testes básicos das regras de avaliação e confiança.

## 14. Possíveis melhorias, caso haja tempo

- **Melhoria 1:** Salvar a melhor pontuação ou o histórico resumido de partidas em arquivo.
- **Melhoria 2:** Adicionar perfis de vagas diferentes, com critérios de avaliação próprios.
- **Melhoria 3:** Criar uma tela inicial e melhorar a apresentação visual com cores, ícones simples e efeitos de feedback, sem tornar o jogo complexo.

## 15. Organização inicial do código

O projeto seguirá a estrutura do template oficial da disciplina:

- `main.py`: inicia o jogo.
- `src/`: funções e módulos da interface, do fluxo da partida e da lógica de avaliação.
- `assets/`: recursos visuais, caso sejam necessários.
- `data/`: dados dos candidatos e possíveis resultados salvos.
- `tests/`: testes simples das funções de cálculo e atualização da confiança.
- `docs/proposta.md`: proposta e planejamento inicial.
- `README.md`: instruções de instalação, execução, regras e créditos.

## 16. Recursos previstos

Serão utilizados **Python**, a biblioteca **Pygame** e o template oficial disponibilizado pela disciplina. Os currículos serão fictícios e elaborados para o jogo. **Não será utilizada IA real** nem serão necessários serviços externos. Se forem utilizados recursos de terceiros, suas origens e licenças serão informadas no `README.md`.

## 17. Originalidade e autoria

O jogo será desenvolvido especificamente para esta atividade, com narrativa, regras e implementação próprias, utilizando o template disponibilizado pela disciplina. Tutoriais, exemplos e ferramentas de apoio poderão ser consultados, mas o projeto não consistirá em uma cópia integral de outro jogo. O estudante deverá compreender e conseguir explicar as principais funções e decisões de implementação.
