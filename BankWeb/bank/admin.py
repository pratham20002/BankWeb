import imp
from django.contrib import admin
from django.dispatch import Signal
from bank.models import Contact

admin.site.register(Contact)
