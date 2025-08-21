from dotenv import load_dotenv
import os
   
load_dotenv()

class Config:
    def __init__(self):
        # Configuración de base de datos
        self.DATABASE_URL: str = os.getenv("DATABASE_URL")
                
        # Configuración de API
        self.API_PREFIX: str = "/api/v1"  
        self.DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
                
        # Configuración de servidor
        self.HOST: str = os.getenv("HOST")
        self.PORT: int = int(os.getenv("PORT"))
        
        self.CORS_ORIGINS: list = os.getenv("CORS_ORIGINS").split(",")
        
config = Config()