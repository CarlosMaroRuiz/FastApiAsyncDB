from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from .core.config import config
from .features import user_router


def create_app() -> FastAPI:
   
    app = FastAPI(
        title="Clean Architecture API",
        description="API RESTful implementada con FastAPI siguiendo los principios de Clean Architecture",
        version="1.0.0",
        docs_url=None,  
        redoc_url=None,
        openapi_url=None,
    )
    
    # Configuración de CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    

    app.include_router(user_router, prefix=config.API_PREFIX)
    

   
    @app.get("/", tags=["root"])
    async def root():
        """Endpoint de bienvenida y estado de la API"""
        return {
            "message": "Bienvenido a la API con Clean Architecture (Async)",
            "version": "1.0.0",
            "status": "online",
            "docs": "/docs"
        }
    
    # Health check para monitoreo
    @app.get("/health", tags=["health"])
    async def health_check():
        """Endpoint para verificar el estado de la API"""
        return {
            "status": "healthy",
            "api": "up",
            "environment": "development" if config.DEBUG else "production"
        }
    
    # Personalización de la documentación
    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=f"{config.API_PREFIX}/openapi.json",
            title="Clean Architecture API - Documentación",
            swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
            swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
        )
    
    @app.get(f"{config.API_PREFIX}/openapi.json", include_in_schema=False)
    async def get_open_api_endpoint():
        return get_openapi(
            title="Clean Architecture API",
            version="1.0.0",
            description="API RESTful con Clean Architecture y FastAPI",
            routes=app.routes,
        )
    
    # Manejador global de excepciones
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        if config.DEBUG:
            return JSONResponse(
                status_code=500,
                content={
                    "error": str(exc),
                    "type": exc.__class__.__name__,
                    "path": request.url.path
                }
            )
        else:
            # En producción no exponemos detalles del error
            return JSONResponse(
                status_code=500,
                content={"error": "Error interno del servidor"}
            )
    
    return app