from api import app, ma

from api.models.aluno_model import AlunoModel
from marshmallow import fields


class AlunoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AlunoModel
        load_instance = True
        fields = ('id', 'nome', 'data_nascimento')

    nome = fields.String(required=True)
    data_nascimento = fields.Date(required=True)
