from flask_restful import Resource
from api import api
from ..schemas import disciplina_schema
from flask import request, make_response, jsonify
from ..dto import disciplina_dto
from ..service import disciplina_service


class DisciplinaController(Resource):
    def get(self):
        disciplina_service_value = disciplina_service.listar_disciplina()
        validate = disciplina_schema.DisciplinaSchema(many=True)
        return make_response(validate.jsonify(disciplina_service_value),200)

    def post(self):
        disciplina_schema_value = disciplina_schema.DisciplinaSchema()
        validate = disciplina_schema_value.validate(request.json)
        if validate:
            return make_response(jsonify(validate),400)
        else:
            nome = request.json["nome"]

            nova_disciplina = disciplina_dto.DisciplinaDTO(nome=nome)
            retorno = disciplina_service.cadastrar_disciplina(nova_disciplina)
            disciplina_json = disciplina_schema_value.jsonify(retorno)
            return make_response(disciplina_json,201)

    def put(self, id):
        disciplina_service_value = disciplina_service.listar_disciplina_by_id(id)
        if disciplina_service_value is None:
            return make_response(jsonify("Disciplina não encontrada"),404)
        disciplina_schema_value = disciplina_schema.DisciplinaSchema()
        validate = disciplina_schema_value.validate(request.json)
        if validate:
            return make_response(jsonify(validate),400)
        else:
            nome = request.json["nome"]
            nova_disciplina = disciplina_dto.DisciplinaDTO(nome=nome)
            disciplina_service.atualizar_disciplina(disciplina_service_value, nova_disciplina)
            disciplina_atualizada = disciplina_service.listar_disciplina_by_id(id)
            return make_response(disciplina_schema_value.jsonify(disciplina_atualizada),200)

    def delete(self, id):
        disciplina_service_value = disciplina_service.listar_disciplina_by_id(id)
        if disciplina_service_value is None:
            return make_response(jsonify("Disciplina não encontrada"), 404)
        disciplina_service.excluir_disciplina(disciplina_service_value)
        return make_response("Disciplina excluída com sucesso!", 204)

class DisciplinaDetailController(Resource):
    def get(self, id):
        disciplina_service_value = disciplina_service.listar_disciplina_by_id(id)
        if disciplina_service_value is None:
            return make_response(jsonify("Disciplina não econtrada!"),404)

        validate = disciplina_schema.DisciplinaSchema()
        return make_response(validate.jsonify(disciplina_service_value),200)


api.add_resource(DisciplinaController, '/disciplina')
api.add_resource(DisciplinaController, '/disciplina/<int:id>',endpoint='alterar_excluir_disciplina',methods=["PUT","DELETE"])
api.add_resource(DisciplinaDetailController, '/disciplina/<int:id>')