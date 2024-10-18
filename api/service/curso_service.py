from ..models import curso_model
from api import db
from .disciplina_service import listar_disciplina_by_id

def cadastrar_curso(curso):
    curso_bd = curso_model.CursoModel(nome=curso.nome, descricao=curso.descricao)
    for i in curso.disciplinas:
        disciplina = listar_disciplina_by_id(i)
        curso_bd.disciplinas.append(disciplina)

    db.session.add(curso_bd)
    db.session.commit()
    return curso_bd

def listar_cursos():
    cursos_bd = curso_model.CursoModel.query.all()
    return cursos_bd

def listar_curso_by_id(pram_id):
    curso_bd = curso_model.CursoModel.query.filter_by(id=pram_id).first()
    return curso_bd

def atualizar_curso(curso_bd, curso_atualizado):
    curso_bd.nome = curso_atualizado.nome
    curso_bd.descricao = curso_atualizado.descricao
    curso_bd.disciplinas = []
    for i in curso_atualizado.disciplinas:
        disciplina = listar_disciplina_by_id(i)
        curso_bd.disciplinas.append(disciplina)

    db.session.commit()

def excluir_curso(curso):
    db.session.delete(curso)
    db.session.commit()
