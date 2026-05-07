<img width="293" height="321" alt="diagrama_atividade" src="https://github.com/user-attachments/assets/dee7299c-19cd-419d-9a7e-cde29146ca77" /><br>

```
@startuml

start
:Selecionar Sessão;
:Informar quantidade de público;

if (Excede capacidade?) then (Sim)
  :Exibir erro;
else (Não)
  :Registrar público;
endif

stop
@enduml
```
