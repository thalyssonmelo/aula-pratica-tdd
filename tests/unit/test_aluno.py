from aluno.aluno import Aluno


# =============================================================
# PARTE 1 — Encontre os bugs
# Escreva um teste para cada bug descrito no guia da atividade.
# =============================================================

def test_calcular_media_considera_a_quantidade_de_notas():
    aluno = Aluno(nome="Ana", notas=[7, 8, 9])

    assert aluno.calcular_media() == 8.0


def test_aluno_com_media_seis_deve_ser_aprovado():
    aluno = Aluno(nome="Bruno", notas=[6, 6, 6, 6])

    assert aluno.situacao() == "Aprovado"


def test_menor_nota_retorna_a_nota_mais_baixa():
    aluno = Aluno(nome="Carla", notas=[8, 5, 9, 7])

    assert aluno.menor_nota() == 5


def test_calcular_media_arredondada_arredonda_para_o_inteiro_mais_proximo():
    aluno = Aluno(nome="Diego", notas=[7, 8, 8, 8])

    assert aluno.calcular_media_arredondada() == 8

# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função


# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método
