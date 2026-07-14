from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

SECRET = os.getenv("INTERNAL_PAGE_SECRET")

@app.get("/")
async def home():
    return FileResponse("index.html")

@app.get("/__internal__/page")
async def internal_page(key: str):
    if key != SECRET:
        raise HTTPException(status_code=404, detail="Not Found")

    return FileResponse("web.html")

@app.get("/__internal__/page")
async def internal_page():
    return FileResponse("web.html")
