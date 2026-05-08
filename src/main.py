from database.connection import get_connection
from repository.sessao_repository import SessaoRepository
from service.sessao_service import SessaoService
from controller.sessao_controller import SessaoController

def main():
    conn = get_connection()

    repository = SessaoRepository(conn)
    service = SessaoService(repository)
    controller = SessaoController(service)

    # Simulação de uso
    sessao_id = 1
    quantidade = 50
    capacidade = 100

    controller.registrar_publico(sessao_id, quantidade, capacidade)

if __name__ == "__main__":
    main()
