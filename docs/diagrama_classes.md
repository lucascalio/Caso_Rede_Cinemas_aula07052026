<img width="218" height="307" alt="diagrama_classes" src="https://github.com/user-attachments/assets/26be661a-0108-41d9-83bc-433bcf85ca95" /><br>

```
@startuml

class Cinema {
  id
  nome
  endereco
  capacidade
}

class Filme {
  id
  titulo
  duracao
  genero
  diretor
}

class Sessao {
  id
  horario
  publico
}

Cinema "1" -- "*" Sessao
Filme "1" -- "*" Sessao

@enduml
```
