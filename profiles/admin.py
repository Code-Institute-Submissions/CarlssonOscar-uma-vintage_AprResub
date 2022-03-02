from django.contrib import admin
from .models import Profiles


@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ("user",)
