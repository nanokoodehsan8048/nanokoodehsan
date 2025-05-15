import os
from pathlib import Path

# BASE_DIR را به درستی تعریف کنید
BASE_DIR = Path(__file__).resolve().parent.parent

# سایر تنظیمات
SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []
DEBUG = True
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',       # حتماً قبل از AuthenticationMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',     # بعد از SessionMiddleware
    'django.contrib.messages.middleware.MessageMiddleware',        # برای سیستم پیام‌های ادمین
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nanokoodehsan.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'home/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# DATABASES تنظیمات دیتابیس SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # مشخص کردن موتور دیتابیس
        'NAME': BASE_DIR / 'db.sqlite3',         # مسیر فایل دیتابیس
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "home/static"
]