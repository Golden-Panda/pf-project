from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Portfolio, PortfolioImage
# Register your models here.

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra=1
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [
        PortfolioImageInline,
    ]

admin.site.register(Portfolio,PortfolioAdmin)