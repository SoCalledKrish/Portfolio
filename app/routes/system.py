from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()


@router.get("/health")
def health():

    return {

        "status": "healthy",

        "application": settings.APP_NAME,

        "version": settings.VERSION,

        "environment": settings.ENVIRONMENT

    }

@router.get("/version")
def version():

    return {

        "application": settings.APP_NAME,

        "version": settings.VERSION

    }

@router.get("/ready")
def ready():

    return {

        "application": settings.APP_NAME,

        "version": settings.VERSION,

        "ready": True

    }

@router.get("/live")
def live():

    return {

        "application": settings.APP_NAME,

        "version": settings.VERSION,

        "live": True

    }