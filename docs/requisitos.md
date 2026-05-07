# Requisitos do Sistema

## Requisitos Funcionais Principais
- Cadastrar cinemas com nome, endereço e capacidade.
- Cadastrar filmes com título, duração, gênero, elenco e diretores.
- Criar sessões vinculando filme, cinema, data e horário.
- Registrar o público de uma sessão.
- Consultar sessões por cinema e por filme.
- Consultar total de público por sessão, por filme e por cinema.
- Consultar dados completos de um filme.

## Regras de Negócio Essenciais
- Cada sessão pertence a um filme e a um cinema.
- Um cinema pode ter várias sessões no mesmo dia.
- O horário da sessão deve respeitar a duração do filme.
- Deve existir um intervalo mínimo entre sessões do mesmo cinema.
- A quantidade registrada de público não pode ultrapassar a capacidade do cinema.
- O total de público de um filme é a soma dos públicos de todas as suas sessões.
- O total de público de um cinema é a soma dos públicos de todas as sessões daquele cinema.
- Um filme pode ter vários gêneros, elenco e diretores.
