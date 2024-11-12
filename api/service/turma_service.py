from ..models import turma_model
from api import db


def cadastrar_turma(turma):
    turma_bd = turma_model.TurmaModel(nome=turma.nome, descricao=turma.descricao, data_inicio=turma.data_inicio, data_fim=turma.data_fim, curso_id=turma.curso_id)
    db.session.add(turma_bd)
    db.session.commit()
    return turma_bd


def listar_turmas():
    turmas = turma_model.TurmaModel.query.all()
    return turmas


def listar_turmas_by_id(param_id):
    turma = turma_model.TurmaModel.query.filter_by(id=param_id).first()
    return turma


def atualizar_turma(turma_bd, turma_atualizada):
    turma_bd.nome = turma_atualizada.nome
    turma_bd.descricao = turma_atualizada.descricao
    turma_bd.data_inicio = turma_atualizada.data_inicio
    turma_bd.data_fim = turma_atualizada.data_fim
    turma_bd.curso_id = turma_atualizada.curso_id
    db.session.commit()


def excluir_turma(turma):
    db.session.delete(turma)
    db.session.commit()
