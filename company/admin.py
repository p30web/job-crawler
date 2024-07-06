from django.contrib import admin
from .models import Company, CompanyCategory


@admin.register(CompanyCategory)
class CompanyCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_fa', 'name_en', 'category', 'size', 'website', 'established_year', 'location')
    list_filter = ('category', 'location')
    search_fields = ('name_fa', 'name_en', 'category__name', 'location__city_name')
