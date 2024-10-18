from dataclasses import field

from marshmallow_sqlalchemy import auto_field

from api import ma
from .. models import curso_model
from marshmallow import fields

class CursoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = curso_model.CursoModel
        load_instance = True
        fields = ('id', 'nome', 'descricao', 'disciplinas')

    nome = auto_field()
    descricao = auto_field()
    disciplinas = auto_field()