import os
import sys
from django.conf import settings
from django.apps import apps

sys.path.append('C:\\Users\\BER\\rojekt\\myproject')  # your project path

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'  # replace 'myproject' with your project name

apps.populate(settings.INSTALLED_APPS)

from new_app_name.models import MyTable  # replace 'new_app_name' with your app name