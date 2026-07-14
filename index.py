from fastapi.responses import FileResponse
from fastapi import HTTPException

@app.get("/")
async def home():
    return FileResponse("index.html")

@app.get("/__internal__/page")
async def internal_page():
    return FileResponse("web.html")

@app.get("/web.html")
async def block_web():
    raise HTTPException(status_code=404, detail="Not Found")
