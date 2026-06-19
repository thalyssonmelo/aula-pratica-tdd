MEDIA_MINIMA_APROVACAO = 6.0
LIMITE_PERCENTUAL_FALTAS = 0.25
SITUACAO_APROVADO = "Aprovado"
SITUACAO_REPROVADO = "Reprovado"
SITUACAO_REPROVADO_POR_FALTA = "Reprovado por falta"
SITUACAO_REPROVADO_POR_NOTA = "Reprovado por nota"


class Aluno:
    def __init__(self, nome: str, notas: list, faltas: int = 0):
        self.nome = nome
        self.notas = notas
        self.faltas = faltas

    def calcular_media(self) -> float:
        return sum(self.notas) / len(self.notas)

    def situacao(self) -> str:
        if self.calcular_media() >= MEDIA_MINIMA_APROVACAO:
            return SITUACAO_APROVADO
        return SITUACAO_REPROVADO

    def maior_nota(self) -> float:
        return max(self.notas)

    def menor_nota(self) -> float:
        return min(self.notas)

    def calcular_media_arredondada(self) -> float:
        return round(self.calcular_media())

    def situacao_final(self, total_aulas: int) -> str:
        percentual_faltas = self.faltas / total_aulas

        if percentual_faltas > LIMITE_PERCENTUAL_FALTAS:
            return SITUACAO_REPROVADO_POR_FALTA
        if self.situacao() == SITUACAO_APROVADO:
            return SITUACAO_APROVADO
        return SITUACAO_REPROVADO_POR_NOTA

    def enviar_boletim(self, email_service) -> None:
        if self.situacao() == SITUACAO_REPROVADO:
            email_service.enviar(self.nome, self.calcular_media())


def contar_aprovados(lista_de_alunos: list[Aluno]) -> int:
    return sum(
        aluno.situacao() == SITUACAO_APROVADO
        for aluno in lista_de_alunos
    )
