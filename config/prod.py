from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-i7-dc_8c0@+%dwnrmq4s!tuu2om3)s^rq+(vqev1cqhu)7o_--$app"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["registros.tekon-rl.cl",'localhost', '127.0.0.1', '[::1]']

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

