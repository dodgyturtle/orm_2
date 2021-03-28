import os
import sys

from dotenv import load_dotenv
from environs import Env

load_dotenv()
env = Env()
env.read_env()

TESTING = sys.argv[1:2] == ["test"]
if TESTING == False:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "HOST": os.getenv("DATABASE_HOST"),
            "PORT": os.getenv("DATABASE_PORT"),
            "NAME": os.getenv("DATABASE_NAME"),
            "USER": os.getenv("DATABASE_USER"),
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "TEST": {
                "NAME": os.path.join(".", "test_db.sqlite3"),
            },
        }
    }
INSTALLED_APPS = ["datacenter"]

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DEBUG = env.bool("DJANGO_DEBUG", default=True)

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ["*"]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
    },
]


USE_L10N = True

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

USE_TZ = True
