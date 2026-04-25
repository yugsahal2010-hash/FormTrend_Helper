from fastapi import FastAPI

app = FastAPI()

@app.post("/weights")
def weights(payload: dict):
    n = payload["n"]
    decay = 0.85
    raw = [decay ** (n - 1 - i) for i in range(n)]
    total = sum(raw)
    result = [w / total for w in raw]
    return {"result": result}
