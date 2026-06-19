from unittest.mock import MagicMock

from aluno.aluno import Aluno
from aluno import aluno as aluno_module


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

def test_contar_aprovados_quando_todos_estao_aprovados():
    alunos = [
        Aluno(nome="Ana", notas=[8, 7, 9, 8]),
        Aluno(nome="Bruno", notas=[6, 6, 7, 7]),
    ]

    assert aluno_module.contar_aprovados(alunos) == 2


def test_contar_aprovados_quando_todos_estao_reprovados():
    alunos = [
        Aluno(nome="Carla", notas=[4, 5, 3, 4]),
        Aluno(nome="Diego", notas=[5, 5, 5, 5]),
    ]

    assert aluno_module.contar_aprovados(alunos) == 0


def test_contar_aprovados_em_lista_mista():
    alunos = [
        Aluno(nome="Elisa", notas=[7, 8, 7, 8]),
        Aluno(nome="Felipe", notas=[4, 5, 4, 5]),
        Aluno(nome="Gabriela", notas=[6, 6, 6, 6]),
    ]

    assert aluno_module.contar_aprovados(alunos) == 2


def test_contar_aprovados_em_lista_vazia():
    assert aluno_module.contar_aprovados([]) == 0


# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método

def test_situacao_final_reprova_por_falta_acima_de_vinte_e_cinco_por_cento():
    aluno = Aluno(nome="Helena", notas=[9, 9, 8, 8], faltas=30)

    assert aluno.situacao_final(total_aulas=100) == "Reprovado por falta"


def test_situacao_final_aprova_com_poucas_faltas_e_media_alta():
    aluno = Aluno(nome="Igor", notas=[7, 8, 7, 8], faltas=10)

    assert aluno.situacao_final(total_aulas=100) == "Aprovado"


def test_situacao_final_reprova_por_nota_com_poucas_faltas_e_media_baixa():
    aluno = Aluno(nome="Julia", notas=[4, 5, 4, 5], faltas=10)

    assert aluno.situacao_final(total_aulas=100) == "Reprovado por nota"


def test_situacao_final_com_exatos_vinte_e_cinco_por_cento_verifica_a_media():
    aluno = Aluno(nome="Lucas", notas=[6, 6, 6, 6], faltas=25)

    assert aluno.situacao_final(total_aulas=100) == "Aprovado"


def test_situacao_final_reprova_por_falta_pouco_acima_de_vinte_e_cinco_por_cento():
    aluno = Aluno(nome="Marina", notas=[9, 9, 9, 9], faltas=26)

    assert aluno.situacao_final(total_aulas=100) == "Reprovado por falta"


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método

def test_enviar_boletim_de_aluno_reprovado_aciona_servico_de_email():
    aluno = Aluno(nome="Nicolas", notas=[4, 5, 4, 5])
    email_service = MagicMock()

    aluno.enviar_boletim(email_service)

    email_service.enviar.assert_called_once_with(
        aluno.nome,
        aluno.calcular_media(),
    )


def test_enviar_boletim_de_aluno_aprovado_nao_aciona_servico_de_email():
    aluno = Aluno(nome="Olivia", notas=[7, 8, 7, 8])
    email_service = MagicMock()

    aluno.enviar_boletim(email_service)

    email_service.enviar.assert_not_called()
