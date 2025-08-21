import uvicorn
from fastapi import FastAPI
from src import create_app,database,config

app:FastAPI = create_app()

@app.on_event("startup")
async def startup_event():
    await database.init_db()

if __name__ == "__main__":
    uvicorn.run("main:app", host=config.HOST, port=config.PORT, reload=config.DEBUG)