from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from manager import Manager
from models import Settings


app = FastAPI()
StradaBOT = Manager()


# Configuração do CORS - Liberado para todas as origens
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Permitir todas as origens
    allow_credentials=True,     # Permitir cookies
    allow_methods=["*"],        # Permitir todos os métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],        # Permitir todos os cabeçalhos
)


@app.get("/stop")
def stop_loop():
    StradaBOT.stop()
    return {"status": "Loop foi parado!"}


@app.get("/start")
def start_loop():
    StradaBOT.start()
    return {"status": "Loop já está rodando!"}


@app.post("/filters")
def set_settings(payload: Settings):
    filters = payload.model_dump()["payload"]
    StradaBOT.set_filters(payload=filters)
    return {"mensagem": "Dados recebidos com sucesso!", "dados": filters}