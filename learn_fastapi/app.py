from http import HTTPStatus

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from learn_fastapi.database import get_session
from learn_fastapi.models import Individual
from learn_fastapi.schemas import IndividualSchema, IndividualSchemaDTO

app = FastAPI()


@app.post(
    '/individual/',
    status_code=HTTPStatus.CREATED,
    response_model=IndividualSchema,
)
def create_user(
    individualDTO: IndividualSchemaDTO, session: Session = Depends(get_session)
):
    individual = Individual(
        name=individualDTO.name,
        email=individualDTO.email,
        document=individualDTO.document,
        document_id=individualDTO.document_id,
    )

    session.add(individual)
    session.commit()
    session.refresh(individual)

    return individual
