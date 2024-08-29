from http import HTTPStatus


def test_should_register_an_individual(client):
    jsonDictionary = {
        'name': 'gustavo',
        'email': 'gus@ta.vo',
        'document': 'cpf',
        'document_id': '06000000000',
    }
    response = client.post('/individual/', json=jsonDictionary)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {**jsonDictionary, 'id': 1}
