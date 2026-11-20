from fastapi import FastAPI
from .database import engine, Base

app = FastAPI(title="KT Docker App")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
def read_root():
    return {"message": "Hello, World! App is working."}

@app.get("/health")
async def health_check():
    return {"status": "ok"}