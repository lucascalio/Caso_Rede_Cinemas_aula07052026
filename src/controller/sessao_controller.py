class SessaoController:

    def __init__(self, service):
        self.service = service

    def registrar_publico(self, sessao_id, quantidade, capacidade):
        try:
            self.service.registrar_publico(sessao_id, quantidade, capacidade)
            print("✅ Público registrado com sucesso!")
        except Exception as e:
            print(f"❌ Erro: {e}")
