from fastapi import FastAPI


app = FastAPI()

@app.get("/getHello")
async def root():
    return {"message": "Hello"}
