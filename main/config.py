import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    TESTING = False
    DEVELOPMENT = True
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'

    FRONTEND_ORIGINS = os.getenv("FRONTEND_ORIGINS")

    DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE_BASE_URL = os.getenv("DATABASE_BASE_URL")
    DATABASE_PORT = os.getenv("DATABASE_PORT")
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_BASE_URL}:{DATABASE_PORT}/{DATABASE_NAME}"


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False


class LocalConfig(Config):
    SECRET_KEY = "local"


class TestingConfig(Config):
    TESTING = True
