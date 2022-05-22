import uvicorn
from fastapi import FastAPI
import api

app = FastAPI()
app.include_router(api.router)

@app.get("/", tags=["Root"])
async def read_root():
    response = {
        "message": "Welcome to this fantastic app!",
    }
    return response

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
