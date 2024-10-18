from flask_restful import Resource

from api import api
from ..schemas import aluno_schema
from flask import request, make_response, jsonify
from ..dto import aluno_dto
from ..service import aluno_service


class AlunoController(Resource):
    def get(self):
        alunos_response_bd = aluno_service.listar_alunos()
        validate = aluno_schema.AlunoSchema(many=True)

        return make_response(validate.jsonify(alunos_response_bd),200)

    def post(self):
        aluno_response_schema = aluno_schema.AlunoSchema()
        validate = aluno_response_schema.validate(request.json)

        if validate:
            return make_response(jsonify(validate),400)

        nome = request.json['nome']
        data_nascimento = request.json['data_nascimento']
        novo_aluno = aluno_dto.AlunoDTO(nome=nome, data_nascimento=data_nascimento)
        retorno = aluno_service.cadastrar_aluno(novo_aluno)
        aluno_json = aluno_response_schema.jsonify(retorno)

        return make_response(aluno_json, 201)

    def put(self,id):
        aluno_response_bd = aluno_service.listar_alunos_by_id(id)

        if aluno_response_bd is None:
            return make_response(jsonify('Aluno não encontrado!'), 404)

        aluno_response_schema = aluno_schema.AlunoSchema()
        validate = aluno_response_schema.validate(request.json)

        if validate:
            return make_response(jsonify(validate),400)

        nome = request.json['nome']
        data_nascimento = request.json['data_nascimento']
        novo_aluno_alterado = aluno_dto.AlunoDTO(nome=nome, data_nascimento=data_nascimento)
        aluno_service.atualizar_aluno(aluno_response_bd, novo_aluno_alterado)
        aluno_atualizado = aluno_service.listar_alunos_by_id(id)

        return make_response(aluno_response_schema.jsonify(aluno_atualizado),200)

    def delete(self,id):
        aluno_response_bd = aluno_service.listar_alunos_by_id(id)

        if aluno_response_bd is None:
            return make_response(jsonify('Aluno não Encontrado!'),400)

        aluno_service.excluir_aluno(aluno_response_bd)

        return make_response('Aluno excluído com sucesso', 204)


class AlunoDetailController(Resource):
    def get(self, id):
        aluno_response_bd = aluno_service.listar_alunos_by_id(id)

        if aluno_response_bd is None:
            return make_response(jsonify('Aluno não encontrado'), 404)

        validate = aluno_schema.AlunoSchema()
        return make_response(validate.jsonify(aluno_response_bd),200)


api.add_resource(AlunoController, '/aluno')
api.add_resource(AlunoController, '/aluno/<int:id>',endpoint='alterar-aluno',methods=["PUT"])
api.add_resource(AlunoController, '/aluno/<int:id>',endpoint='excluir-aluno',methods=["DELETE"])
api.add_resource(AlunoDetailController, '/aluno/<int:id>')