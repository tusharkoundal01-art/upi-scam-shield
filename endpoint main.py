from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "success", "message": "Server connected!"}

@app.get("/upi-status")
def get_upi_status():
    return {"status": "active", "payment_gateway": "UPI"}