from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello world "}

@app.get("/test/<nombre>")
async def test():
    liste = [i for i in range(10)]
    return {"liste de range(10)" : liste}