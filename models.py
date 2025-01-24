from pydantic import BaseModel


#  Definição do modelo de dados esperado no JSON
class Settings(BaseModel):
    origens_1: list
    origens_2: list