from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)

templates = Jinja2Templates(directory="templates")
 
SECRET = os.getenv("INTERNAL_PAGE_SECRET")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "secret": SECRET
        }
    )


@app.get("/__internal__/page")
async def internal_page(key: str):
    if key != SECRET:
        raise HTTPException(status_code=404, detail="Not Found")

    return FileResponse("web.html")


@app.get("/web.html")
async def block_web():
    raise HTTPException(status_code=404, detail="Not Found")
