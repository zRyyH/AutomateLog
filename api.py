from fastapi import FastAPI
from strada import StradaLog
from models import Settings


app = FastAPI()


StradaBOT = StradaLog()
StradaBOT.run_loop()


@app.get("/stop")
def stop_loop():
    StradaBOT.start_stop(state=False)
    return {"status": "Loop parado"}

@app.get("/start")
def start_loop():
    StradaBOT.start_stop(state=True)
    return {"status": "Loop já está rodando"}

@app.post("/set")
def stop_loop(payload: Settings):
    StradaBOT.set_settings(payload=payload)
    return {
        "mensagem": "Dados recebidos com sucesso!",
        "dados": payload.dict()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000, host='192.168.3.250')