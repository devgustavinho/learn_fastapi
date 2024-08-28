from pydantic import BaseModel, EmailStr


class IndividualSchemaDTO(BaseModel):
    name: str
    email: EmailStr
    document: str
    document_id: str


class IndividualSchema(IndividualSchemaDTO):
    id: int
