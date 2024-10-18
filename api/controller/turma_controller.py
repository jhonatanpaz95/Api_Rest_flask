from flask_restful import Resource
from sqlalchemy.orm import validates
from api import api
from ..schemas import turma_schema
from flask import request, make_response, jsonify
from ..dto import turma_dto
from ..service import turma_service



class TurmaController(Resource):
    def get(self):
        turma_response_bd = turma_service.listar_turmas()
        validate = turma_schema.TurmaSchema(many=True)

        return make_response(validate.jsonify(turma_response_bd),200)

    def post(self):
        turma_response_schema = turma_schema.TurmaSchema()
        validate = turma_response_schema.validate(request.json)

        if validate:
            return make_response(jsonify(validate),400)

        nome = request.json['nome']
        data_inicio = request.json['data_inicio']
        data_fim = request.json['data_fim']
        descricao = request.json['descricao']
        curso_id = request.json['curso_id']
        nova_turma = turma_dto.TurmaDTO(nome=nome, descricao=descricao, data_inicio=data_inicio, data_fim=data_fim, curso_id=curso_id)
        retorno = turma_service.cadastrar_turma(nova_turma)
        turma_json = turma_response_schema.jsonify(retorno)

        return make_response(turma_json,201)

    def put(self, id):
        turma_response_bd = turma_service.listar_turmas_by_id(id)

        if turma_response_bd is None:
            return make_response(jsonify('Turma não encontrada'),404)

        turma_response_schema = turma_schema.TurmaSchema()
        validate = turma_response_schema.validate(request.json)

        if validate:
            return make_response(jsonify(validate),400)

        nome = request.json['nome']
        data_inicio = request.json['data_inicio']
        data_fim = request.json['data_fim']
        descricao = request.json['descricao']
        curso_id = request.json['curso_id']
        nova_turma = turma_dto.TurmaDTO(nome=nome, descricao=descricao, data_inicio=data_inicio, data_fim=data_fim, curso_id=curso_id)
        turma_service.atualizar_turma(turma_response_bd, nova_turma)
        turma_atalizada = turma_service.listar_turmas_by_id(id)

        return make_response(turma_response_schema.jsonify(turma_atalizada),200)


    def delete(self, id):
        turma_response_bd = turma_service.listar_turmas_by_id(id)

        if turma_response_bd is None:
            return make_response(jsonify('Turma não encontrada'), 404)

        turma_service.excluir_turma(turma_response_bd)

        return make_response('Turma excluída com sucesso!', 204)

class TurmaDetailController(Resource):
    def get(self, id):
        turma_response_bd = turma_service.listar_turmas_by_id(id)

        if turma_response_bd is None:
            return make_response(jsonify('Turma não econtrada!'),404)

        validate = turma_schema.TurmaSchema()

        return make_response(validate.jsonify(turma_response_bd),200)


api.add_resource(TurmaController, '/turma')
api.add_resource(TurmaController, '/turma/<int:id>',endpoint='alterar_excluir_turma',methods=["PUT","DELETE"])
api.add_resource(TurmaDetailController, '/turma/<int:id>')
