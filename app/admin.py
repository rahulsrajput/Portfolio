from django.contrib import admin
from .models import Contact, Project, Category, Blog, Home, WorkExperience, Education, Certification

# Register your models here.

# admin.site.register(Contact)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','link']


# @admin.site.register(Project)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'projectName','technologies']


# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


# admin.site.register(Blog)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'blogTitle' ,'category', 'totalViews', 'datePublished']



admin.site.register(Home)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Certification)
