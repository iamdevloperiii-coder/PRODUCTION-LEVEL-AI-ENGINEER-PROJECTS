# (c) 2026 Mohammad Subhan Pasha - SUBHAN
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(title="SUBHAN-INFERNO")
class ChatReq(BaseModel):
    prompt: str
    user_id: str
@app.get("/health")
def health(): return {"status": "LIVE", "latency_ms": 12, "owner": "SUBHAN"}
@app.post("/chat")
def chat(req: ChatReq): return {"answer": f"SUBHAN-INFERNO processed: {req.prompt}", "latency_ms": 45, "model": "subhan-inferno-v1"}
if __name__ == "__main__":
    print("SUBHAN-INFERNO Ready - Run: uvicorn main:app --port 8000")
    print(health())
