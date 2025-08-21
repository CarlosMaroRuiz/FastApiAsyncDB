
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .base import Base

class DatabaseSession:
    engine: AsyncEngine
    Session: sessionmaker
    
    def __init__(self, url: str):
        self.engine = create_async_engine(url, echo=True)
        self.Session = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )
    
    async def create_session(self) -> AsyncSession:
        """Crea y devuelve una sesión de base de datos."""
        # IMPORTANTE: Debe devolver una sesión, no un generador
        return self.Session()  # Devuelve directamente la sesión
    
    async def init_db(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)