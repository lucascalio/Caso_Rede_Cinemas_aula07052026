<img width="646" height="444" alt="diagrama_sequencia" src="https://github.com/user-attachments/assets/13de35cb-a969-432d-bc5a-4e3ca2abb54f" /><br>

```
@startuml

actor Usuario

Usuario -> View : informarPublico()
View -> Controller : registrarPublico()
Controller -> Service : validarDados()
Service -> Repository : salvarPublico()
Repository -> DB : INSERT
DB --> Repository : OK
Repository --> Service : OK
Service --> Controller : OK
Controller --> View : sucesso

@enduml
```
