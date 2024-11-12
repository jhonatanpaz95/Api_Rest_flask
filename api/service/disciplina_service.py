from ..models import disciplina_model
from api import db


def cadastrar_disciplina(disciplina):
    disciplina_bd = disciplina_model.DisciplinaModel(nome=disciplina.nome)
    db.session.add(disciplina_bd)
    db.session.commit()
    return disciplina_bd


def listar_disciplina():
    disciplinas = disciplina_model.DisciplinaModel.query.all()
    return disciplinas


def listar_disciplina_by_id(param_id):
    disciplina = disciplina_model.DisciplinaModel.query.filter_by(id=param_id).first()
    return disciplina


def atualizar_disciplina(disciplina_bd, disciplina_atualizada):
    disciplina_bd.nome = disciplina_atualizada.nome
    db.session.commit()


def excluir_disciplina(disciplina):
    db.session.delete(disciplina)
    db.session.commit()
