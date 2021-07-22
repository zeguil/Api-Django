from django.contrib import admin
from api.models import Student

class Students(admin.ModelAdmin):
    list_display = ('id', 'name','age', 'document')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Student, Students)