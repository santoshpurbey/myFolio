from django.contrib import admin
from models import Project, Category, Skill, ProjectImage, Post, Comment, PostLayout

# set up automated slug creation
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('name', 'short_description', 'client', 'layouts')
    prepopulated_fields = {'slug': ('name',)}

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'publish', 'status', 'layouts')
    prepopulated_fields = {'slug':('title',)}

class SkillAdmin(admin.ModelAdmin):
    model = Skill
    prepopulated_fields = {'slug':('name',)}

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = { 'slug':('name',)}

class PostLayoutAdmin(admin.ModelAdmin):
    model = PostLayout
    prepopulated_fields = { 'slug':('name',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

# Register your models here.

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Skill)
admin.site.register(ProjectImage)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PostLayout, PostLayoutAdmin)
