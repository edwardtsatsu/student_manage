import os
from configs.settings import settings

SECRET_KEY = settings.secret_key

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

JWT_SECRET_KEY = settings.jwt_secret_key

UPLOAD_FOLDER = basedir.join('public/images')
