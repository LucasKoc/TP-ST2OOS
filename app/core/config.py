import os

class Settings:
    """App settings"""
    PROJECT_NAME = "FastAPI - CarService"
    PROJECT_VERSION = "0.1.0"

    MYSQL_USER = os.getenv("DATABASE_USER")
    MYSQL_PASSWORD = os.getenv("DATABASE_PASSWORD")
    MYSQL_HOST = os.getenv("DATABASE_HOST")
    MYSQL_PORT = os.getenv("DATABASE_PORT")
    MYSQL_DATABASE = os.getenv("DATABASE_NAME")

    DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

settings = Settings()
