from ..core.database.session import DatabaseSession
from ..core.config import config

database: DatabaseSession = DatabaseSession(config.DATABASE_URL)

async def get_db_session():
    """
    Crea y proporciona una sesión de base de datos asíncrona.
    """
    
    session = await database.create_session()
    try:
        yield session
    finally:
        await session.close()