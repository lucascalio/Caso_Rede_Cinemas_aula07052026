from model.sessao import Sessao

class SessaoService:

    def __init__(self, repository):
        self.repository = repository

    def registrar_publico(self, sessao_id, quantidade, capacidade):
        sessao = Sessao(sessao_id, "", 0, capacidade)

        if not sessao.validar_capacidade(quantidade):
            raise Exception("Capacidade excedida")

        self.repository.salvar_publico(sessao_id, quantidade)
