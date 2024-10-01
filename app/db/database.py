from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# SQLAlchemy setup for MySQL connection
DATABASE_URL = settings.DATABASE_URL

# Create the SQLAlchemy engine for MySQL
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True  # This ensures connections are checked before use
)

# Create a configured "SessionLocal" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
