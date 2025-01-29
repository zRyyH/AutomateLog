from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strada import StradaLog
from models import Settings

app = FastAPI()


# Configuração do CORS - Liberado para todas as origens
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,  # Permitir cookies
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

StradaBOT = StradaLog()


@app.get("/reset")
def reset():
    print("RESET")
    StradaBOT.start_stop(state=False)
    StradaBOT.set_settings(payload=[])
    return {"status": "Resetado"}

@app.get("/stop")
def stop_loop():
    print("STOP")
    StradaBOT.start_stop(state=False)
    return {"status": "Loop parado"}

@app.get("/start")
def start_loop():
    print("START")
    StradaBOT.start_stop(state=True)
    StradaBOT.run_loop()
    print('running definido como:', True)
    return {"status": "Loop já está rodando"}

@app.post("/set")
def set_settings(payload: Settings):
    settings_data = payload.model_dump()['payload']
    StradaBOT.set_settings(payload=settings_data)
    return {"mensagem": "Dados recebidos com sucesso!", "dados": settings_data}