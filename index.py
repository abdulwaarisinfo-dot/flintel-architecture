from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def home(): 
    return FileResponse("index.html")

@app.get("/__internal__/page")
async def internal_page():
    return FileResponse("web.html")

@app.get("/web.html")
async def block_web():
    raise HTTPException(status_code=404, detail="Not Found")
