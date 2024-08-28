from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from learn_fastapi.schemas import IndividualSchema, IndividualSchemaDTO

app = FastAPI()

Database: list[IndividualSchema] = [
    IndividualSchema(
        id=1,
        name='Gustavo',
        email='gusta@vo.carneiro',
        document='cpf',
        document_id='06124721589791',
    ),
    IndividualSchema(
        id=2,
        name='Gustavo',
        email='gusta@vo.carneiro',
        document='cpf',
        document_id='06124721589791',
    ),
]


@app.get('/', response_model=list[IndividualSchema])
def get_all_users():
    return Database


@app.get('/{id}', response_model=IndividualSchema)
def get_user(id: int):
    if id > len(Database) or id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='user_not_found'
        )

    return Database[id - 1]


@app.post('/', status_code=HTTPStatus.CREATED, response_model=IndividualSchema)
def create_user(individualDTO: IndividualSchemaDTO):
    user = IndividualSchema(**individualDTO.model_dump(), id=len(Database) + 1)
    Database.append(user)

    return user
