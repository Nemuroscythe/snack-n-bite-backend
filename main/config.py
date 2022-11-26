# Configuration / variables d'environnements pour le développement local

DEVELOPMENT = True
DEBUG = True
CSRF_ENABLED = True
SECRET_KEY = 'this-really-needs-to-be-changed'

BASE_URL = 'localhost'
DATABASE_PORT = '5432'
USERNAME = 'snack-n-bite-backend'
PASSWORD = 'SnackNBitePassW00rd'
DATABASE = 'snack-n-bite'
SQLALCHEMY_DATABASE_URI = f"postgresql://{USERNAME}:{PASSWORD}@{BASE_URL}:{DATABASE_PORT}/{DATABASE}"
