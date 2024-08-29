from sqlalchemy import select

from learn_fastapi.models import Individual


def test_create_user(session):
    new_individual = Individual(
        name='Gustavo',
        email='gustavo@carn.eiro',
        document='cpf',
        document_id='06100000000',
    )
    session.add(new_individual)
    session.commit()

    user = session.scalar(
        select(Individual).where(Individual.email == 'gustavo@carn.eiro')
    )

    assert new_individual.email == user.email
