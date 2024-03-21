from django.contrib import admin
from .models import Subscription

# Register your models here.
@admin.register(Subscription)
class SubAdmin(admin.ModelAdmin):
    pass