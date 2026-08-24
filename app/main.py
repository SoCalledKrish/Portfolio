from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes.home import router as home_router
from app.routes.system import router as system_router
from app.core.logger import logger

app = FastAPI(
    title="CloudForge",
    description="Personal DevOps Portfolio",
    version="1.0.0",
)

# Static Files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.on_event("startup")
async def startup():

    logger.info("Application started")

@app.on_event("shutdown")
async def shutdown():

    logger.info("Application stopped")

# Routes
app.include_router(home_router)
app.include_router(system_router)
logger.info("Abhiram portfolio starting...")