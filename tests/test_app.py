from http import HTTPStatus

from learn_fastapi.schemas import IndividualSchema

test_init_database_reponse = [
    IndividualSchema(
        id=1,
        name='Gustavo',
        email='gusta@vo.carneiro',
        document='cpf',
        document_id='06124721589791',
    ).__dict__,
    IndividualSchema(
        id=2,
        name='Gustavo',
        email='gusta@vo.carneiro',
        document='cpf',
        document_id='06124721589791',
    ).__dict__,
]


def test_should_get_all_clients(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == test_init_database_reponse


def test_should_create_a_client(client):
    body = {
        'name': 'gustavo',
        'email': 'gus@ta.vo',
        'document': 'cpf',
        'document_id': '06100000000',
    }
    response = client.post('/', json=body)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {**body, 'id': 3}

    body = {
        'name': 'gustavo',
        'email': 'gus@ta.vo',
        'document': 'cpf',
        'document_id': '06100000000',
    }
    response = client.post('/', json=body)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {**body, 'id': 4}


def test_should_retrieve_a_client(client):
    response = client.get('/2')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == test_init_database_reponse[1]


def test_should_retrieve_an_error_when_invalid_client_id(client):
    response = client.get('/20')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'user_not_found'}
