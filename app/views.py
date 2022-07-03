import requests
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {"message": "App2 start"}
