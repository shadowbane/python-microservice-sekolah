from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from app.routes import api

# Initialize the app
app = FastAPI()

app.include_router(api.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)
