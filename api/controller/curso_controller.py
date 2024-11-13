from flask_restful import Resource
from api import api


from ..schemas import curso_schema
from flask import request, make_response, jsonify
from ..dto import curso_dto
from ..service import curso_service


class CursoController(Resource):
    def get(self):
        curso_response_bd = curso_service.listar_cursos()
        validate = curso_schema.CursoSchema(many=True)

        return make_response(validate.jsonify(curso_response_bd), 200)

    def post(self):
        curso_response_schema = curso_schema.CursoSchema()
        validate = curso_response_schema.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)

        nome = request.json['nome']
        descricao = request.json['descricao']
        disciplinas = request.json['disciplinas']
        novo_curso = curso_dto.CursoDTO(nome=nome, descricao=descricao, disciplinas=disciplinas)
        retorno = curso_service.cadastrar_curso(novo_curso)
        curso_json = curso_response_schema.jsonify(retorno)

        return make_response(curso_json, 201)

    def put(self, id):
        curso_response_bd = curso_service.listar_curso_by_id(id)

        if curso_response_bd is None:
            return make_response(jsonify('Curso não encontrado'), 404)

        curso_response_schema = curso_schema.CursoSchema()
        validate = curso_response_schema.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)

        nome = request.json['nome']
        descricao = request.json['descricao']
        disciplinas = request.json['disciplinas']
        novo_curso_alterado = curso_dto.CursoDTO(nome=nome, descricao=descricao, disciplinas=disciplinas)
        curso_service.atualizar_curso(curso_response_bd, novo_curso_alterado)
        curso_atualizado = curso_service.listar_curso_by_id(id)

        return make_response(curso_response_schema.jsonify(curso_atualizado), 200)

    def delete(self, id):
        curso_response_bd = curso_service.listar_curso_by_id(id)

        if curso_response_bd is None:
            return make_response(jsonify('Curso não encontrado!'), 400)

        curso_service.excluir_curso(curso_response_bd)

        return make_response('Aluno excluído com sucesso', 204)


class CursoDetailController(Resource):
    def get(self, id):
        curso_response_bd = curso_service.listar_curso_by_id(id)

        if curso_response_bd is None:

            return make_response(jsonify('Curso não encontrado!'), 404)

        validate = curso_schema.CursoSchema()

        return make_response(validate.jsonify(curso_response_bd), 200)


api.add_resource(CursoController, '/curso')
api.add_resource(CursoController, '/curso/<int:id>', endpoint='alterar-excluir-curso', methods=["PUT", "DELETE"])
api.add_resource(CursoDetailController, '/curso/<int:id>')
