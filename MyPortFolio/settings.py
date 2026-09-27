"""
Django settings for MyPortFolio project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Loads variables from a local ".env" file (if present) into the
# environment, so DJANGO_SECRET_KEY etc. below can pick them up.
load_dotenv(BASE_DIR / ".env")

# ---------------------------------------------------------------------------
# Security
# ---------------------------------------------------------------------------
# SECRET_KEY and DEBUG now come from environment variables so nothing secret
# is ever committed to git. Create a local ".env" file (see .env.example) or
# set these as real environment variables on your host (Render, Railway, etc).

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    # Fallback ONLY for first-time local setup — replace this by setting
    # DJANGO_SECRET_KEY in your environment before deploying anywhere public.
    "django-insecure-CHANGE-ME-set-DJANGO_SECRET_KEY-env-var",
)

DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

ALLOWED_HOSTS = [
    h.strip() for h in os.environ.get(
        "DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost"
    ).split(",") if h.strip()
]

# ---------------------------------------------------------------------------
# Application definition
# ---------------------------------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MyPortFolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MyPortFolio.wsgi.application'

# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------
# Defaults to SQLite so the project runs with zero extra setup. Set
# DJANGO_DB_ENGINE=mysql (plus the other DJANGO_DB_* vars) to use MySQL
# instead — nothing about this ever needs to be hardcoded in this file.

if os.environ.get("DJANGO_DB_ENGINE") == "mysql":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get("DJANGO_DB_NAME", "portfolio"),
            'USER': os.environ.get("DJANGO_DB_USER", "root"),
            'PASSWORD': os.environ.get("DJANGO_DB_PASSWORD", ""),
            'HOST': os.environ.get("DJANGO_DB_HOST", "localhost"),
            'PORT': os.environ.get("DJANGO_DB_PORT", "3306"),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ---------------------------------------------------------------------------
# Password validation
# ---------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------------------------------------------------------------------------
# Internationalization
# ---------------------------------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# ---------------------------------------------------------------------------
# Static & media files
# ---------------------------------------------------------------------------

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / 'main/static']

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
    'RAW_FILE_EXTENSIONS': ['pdf', 'doc', 'docx', 'zip', 'txt'],
}

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# Whitenoise's manifest storage is strict about every file referenced in CSS
# actually existing after collectstatic. Some Django admin static files
# (debug-only icons) aren't always present, so we relax this check.
WHITENOISE_MANIFEST_STRICT = False

# Backward-compat: django-cloudinary-storage's collectstatic override still
# reads the old STATICFILES_STORAGE attribute directly (Django 6 removed it),
# so we set it manually here to avoid AttributeError during collectstatic.
STATICFILES_STORAGE = STORAGES["staticfiles"]["BACKEND"]

# Uploaded content (profile photo, project thumbnails, blog covers, resume).
# NOTE: on most free-tier hosts (Render, Railway, etc.) local disk storage is
# wiped on every deploy/restart. Now using Cloudinary for persistent storage.
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'