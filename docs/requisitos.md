# Levantamento de Requisitos

## Requisitos Funcionais (RF)

- **RF01**: Cadastrar cinemas  
- **RF02**: Cadastrar filmes  
- **RF03**: Cadastrar sessões  
- **RF04**: Registrar público por sessão  
- **RF05**: Consultar filmes em cartaz por cinema  
- **RF06**: Consultar público total:
  - por sessão  
  - por filme  
  - por cinema  
- **RF07**: Consultar detalhes de filmes (gênero, elenco, diretor)  

---

## Regras de Negócio (RN)

- **RN01**: Uma sessão deve estar vinculada a um filme e a um cinema  
- **RN02**: O horário da sessão deve respeitar a duração do filme  
- **RN03**: Deve existir intervalo mínimo entre sessões (ex: 15 minutos)  
- **RN04**: O público não pode exceder a capacidade do cinema  
- **RN05**: Um filme pode estar em vários cinemas  
- **RN06**: Cada sessão possui apenas um filme  
