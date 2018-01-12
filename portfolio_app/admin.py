from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Portfolio, PortfolioImage
from django.utils.text import slugify
# Register your models here.

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra=1
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title','slug','created','modified','link')
    list_display_links = ('slug',)
    prepopulated_fields={
        "slug":("title",)
    }
    
    inlines = [
        PortfolioImageInline,
    ]

admin.site.register(Portfolio,PortfolioAdmin)
