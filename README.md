# Sistema de Rede de Cinemas

## Descrição

Este projeto consiste no desenvolvimento de um sistema para gerenciamento de uma rede de cinemas, permitindo o controle de filmes em cartaz, sessões e público.

O sistema foi desenvolvido como parte da disciplina de Engenharia de Software, com foco na aplicação de conceitos de modelagem UML e arquitetura em camadas.

---

## Objetivo

- Modelar um problema real de software  
- Aplicar diagramas UML de forma integrada  
- Implementar um sistema seguindo boas práticas  
- Utilizar arquitetura em camadas (MVC + Service + Repository)  

---

## Arquitetura do Sistema

O sistema foi desenvolvido utilizando:

- MVC (Model - View - Controller)  
- Service Layer (Regras de Negócio)  
- Repository Pattern (Acesso a Dados)  
- SQLite (Persistência)  

### Organização das Camadas

- Model → Representa as entidades do domínio  
- Controller → Recebe e trata as entradas  
- Service → Contém as regras de negócio  
- Repository → Responsável pela persistência  
- Database → Conexão com o banco de dados  

---

## Funcionalidades

- Cadastro de cinemas  
- Cadastro de filmes  
- Cadastro de sessões  
- Registro de público por sessão  
- Consulta de filmes em cartaz por cinema  
- Consulta de público:
  - por sessão  
  - por filme  
  - por cinema  
- Consulta de detalhes dos filmes  

---

## Regras de Negócio

- Uma sessão deve estar vinculada a um filme e a um cinema  
- O horário da sessão deve respeitar a duração do filme  
- Deve existir intervalo mínimo entre sessões  
- O público não pode exceder a capacidade do cinema  
- Um filme pode estar em vários cinemas  
- Cada sessão possui apenas um filme  

---

## Estrutura do Projeto

```
cinema-system/
│
├── docs/
│   ├── casos-de-uso.puml
│   ├── classes.puml
│   ├── atividade.puml
│   ├── sequencia.puml
│   └── requisitos.md
│
├── src/
│   ├── model/
│   ├── controller/
│   ├── service/
│   ├── repository/
│   ├── database/
│   └── main.py
│
└── README.md
```

---

## Diagramas UML

Os diagramas estão disponíveis na pasta `/docs`:

- Diagrama de Casos de Uso  
- Diagrama de Classes  
- Diagrama de Atividade  
- Diagrama de Sequência  

---

## Banco de Dados

O sistema utiliza SQLite como banco de dados.

### Criação do banco

```bash
sqlite3 cinema.db < src/database/schema.sql
```

---

## Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/Caso_Rede_Cinemas_aula070526.git
```

2. Acesse a pasta:

```bash
cd Caso_Rede_Cinemas_aula070526
```

3. Crie o banco de dados:

```bash
sqlite3 cinema.db < src/database/schema.sql
```

4. Execute o sistema:

```bash
python src/main.py
```

---

## Tecnologias Utilizadas

- Python  
- SQLite  
- PlantUML  
