# cal/admin.py

from django.contrib import admin
# from cal.models import Event
from .models import Event

admin.site.register(Event)