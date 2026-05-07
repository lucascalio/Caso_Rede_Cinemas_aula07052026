# Sistema de Rede de Cinemas

Projeto acadêmico da disciplina de Engenharia de Software.

## Objetivo
Desenvolver um sistema de informação para uma rede de cinemas, permitindo o controle de filmes, sessões e público, com organização dos dados e aplicação de UML integrada à implementação.

## Contexto do Problema
A empresa possui diversas unidades em diferentes cidades e estados. Cada cinema possui endereço, capacidade e programação própria, com sessões distribuídas ao longo do dia.

O sistema deve apoiar:
- controle dos filmes em exibição por cinema;
- organização das sessões respeitando duração e intervalos;
- registro diário do público;
- totalização de público por sessão, filme e cinema;
- consulta de elenco, diretores e gêneros.

## Arquitetura
O projeto foi desenvolvido com a seguinte organização:

View → Controller → Service → Repository → SQLite

## Estrutura do Projeto
- `docs/`: documentação e diagramas UML
- `database/`: conexão e banco SQLite
- `src/`: código-fonte da aplicação
- `main.py`: execução principal

## Funcionalidades implementadas
- Criar sessão
- Listar sessões
- Registrar público de uma sessão
- Validação de capacidade do cinema

## Diagramas UML
Os diagramas estão disponíveis na pasta `docs/`:
- Casos de uso
- Classes
- Atividade
- Sequência

## Como executar
1. Abra o terminal na raiz do projeto.
2. Execute:

```bash
python main.py
