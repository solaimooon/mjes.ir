from django.contrib import admin
from .models import *
@admin.register(Mosque)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Hall)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Facility)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
