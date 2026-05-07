<img width="500" height="552" alt="casos_de_uso" src="https://github.com/user-attachments/assets/fa5bc8dc-890c-41a9-b157-933e0f8c32b4" /><br>

```
@startuml
left to right direction

actor "Funcionário/Administrador" as Admin
actor "Espectador" as User

rectangle Sistema {
    Admin --> (Cadastrar Cinema)
    Admin --> (Cadastrar Filme)
    Admin --> (Cadastrar Sessão)
    Admin --> (Registrar Público)

    User --> (Consultar Filmes em Cartaz)
    User --> (Consultar Detalhes do Filme)
    User --> (Consultar Público)
}
@enduml
```
