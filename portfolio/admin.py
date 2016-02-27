from django.contrib import admin
from models import Project, Category, Skill, ProjectImage


# set up automated slug creation
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(ProjectImage)
