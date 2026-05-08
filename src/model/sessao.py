class Sessao:
    def __init__(self, id, horario, publico, capacidade):
        self.id = id
        self.horario = horario
        self.publico = publico
        self.capacidade = capacidade

    def validar_capacidade(self, quantidade):
        return quantidade <= self.capacidade
