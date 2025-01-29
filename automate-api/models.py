from pydantic import BaseModel


#  Definição do modelo de dados esperado no JSON
class Settings(BaseModel):
    payload: list