SITUACAO_APROVADO = "Aprovado"


class Aluno:
    def __init__(self, nome: str, notas: list, faltas: int = 0):
        self.nome = nome
        self.notas = notas
        self.faltas = faltas

    def calcular_media(self) -> float:
        return sum(self.notas) / len(self.notas)

    def situacao(self) -> str:
        if self.calcular_media() >= 6.0:
            return SITUACAO_APROVADO
        return "Reprovado"

    def maior_nota(self) -> float:
        return max(self.notas)

    def menor_nota(self) -> float:
        return min(self.notas)

    def calcular_media_arredondada(self) -> float:
        return round(self.calcular_media())


def contar_aprovados(lista_de_alunos: list[Aluno]) -> int:
    return sum(
        aluno.situacao() == SITUACAO_APROVADO
        for aluno in lista_de_alunos
    )
