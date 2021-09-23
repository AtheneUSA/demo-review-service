import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

def start():
    uvicorn.run("review_service.main:app", host="0.0.0.0", port=8001, reload=True)

if __name__ == "__main__":
    start()
