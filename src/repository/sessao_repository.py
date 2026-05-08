class SessaoRepository:

    def __init__(self, conn):
        self.conn = conn

    def salvar_publico(self, sessao_id, publico):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE sessao SET publico = ? WHERE id = ?",
            (publico, sessao_id)
        )
        self.conn.commit()

    def buscar_sessao(self, sessao_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, horario, publico FROM sessao WHERE id = ?", (sessao_id,))
        return cursor.fetchone()
