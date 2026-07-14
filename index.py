from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)

@app.get("/")
async def home():
    return FileResponse("templates/index.html")


@app.get("/__internal__/page")
async def internal_page():
    return FileResponse("templates/web.html")


@app.get("/__internal__/page")
async def block_web():
    raise HTTPException(status_code=404, detail="Not Found")
