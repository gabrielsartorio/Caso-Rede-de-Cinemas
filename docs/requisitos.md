# Requisitos e Regras de Negócio - Rede de Cinemas

## Requisitos Funcionais
- **RF01:** O sistema deve permitir cadastrar, consultar, atualizar e remover filmes.
- **RF02:** O sistema deve permitir cadastrar e consultar cinemas (capacidade, nome e local).
- **RF03:** O sistema deve permitir cadastrar sessões associando filme, cinema, horário e preço do ingresso.
- **RF04:** O sistema deve registrar espectadores em uma sessão e totalizar o público.

## Regras de Negócio
- **RN01:** Não pode haver sobreposição de horários para sessões no mesmo cinema (com intervalo mínimo de 15 minutos).
- **RN02:** O público registrado em uma sessão não pode ultrapassar a capacidade do cinema.
