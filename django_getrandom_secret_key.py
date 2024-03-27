# https://www.makeuseof.com/django-secret-key-generate-new/
# import the get_random_secret_key() function
from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()
print(secret_key)