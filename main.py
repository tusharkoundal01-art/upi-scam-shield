from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Root is working"}

@app.get("/upi-status")
def upi_status():
    return {"status": "active"}