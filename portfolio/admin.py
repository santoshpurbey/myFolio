from django.contrib import admin
from models import Project, Category, Skill, ProjectImage, Post, Tag


# set up automated slug creation
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'publish', 'status',)
    prepopulated_fields = {'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = { 'slug':('name',)}

class TagAdmin(admin.ModelAdmin):
    model = Tag
    prepopulated_fields = { 'slug':('name',)}

# Register your models here.

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Skill)
admin.site.register(ProjectImage)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
