from database.connection import create_tables
from src.repositories.sessao_repository import SessaoRepository
from src.services.sessao_service import SessaoService
from src.controllers.sessao_controller import SessaoController
from src.views.console_view import ConsoleView


def main():
    create_tables()

    repository = SessaoRepository()
    service = SessaoService(repository)
    controller = SessaoController(service)
    view = ConsoleView()

    while True:
        opcao = view.menu()

        try:
            if opcao == "1":
                dados = view.criar_sessao()
                controller.criar_sessao(*dados)

            elif opcao == "2":
                sessoes = repository.listar_sessoes()
                view.mostrar_sessoes(sessoes)

            elif opcao == "3":
                dados = view.registrar_publico()
                controller.registrar_publico(*dados)

            elif opcao == "0":
                break

        except Exception as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
