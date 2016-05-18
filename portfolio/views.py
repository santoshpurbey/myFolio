from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import Http404
from django.shortcuts import render, redirect
from django.template.context import RequestContext
from django.utils import timezone
from .models import Project, Skill, Category, ProjectImage, Post, Tag

def about(request):
    return render( request, 'about.html', {} )

def portfolio_list(request):
    projects = Project.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
    return render(request, 'portfolio/portfolio_list.html', {'projects': projects})

def portfolio_detail(request, pk):
    project = Project.objects.get(pk=pk)
    skills = Skill.objects.filter(project__pk=pk)
    categories = Category.objects.filter(project__pk=pk)
    project_images = ProjectImage.objects.filter(project__pk=pk)

    return render(
        request,
        'portfolio/portfolio_detail.html',
        {
            'project': project,
            'skills': skills,
            'categories': categories,
            'project_images': project_images
        }
    )

def contact(request):
    return render( request, 'contact.html', {})

def blog_list(request):
    posts = Post.objects.all()
    return render( request, 'blog/blog_list.html', {'posts' : posts })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    #grub categories
    categories = Category.objects.all()
    #grub Tags
    tags = Tag.objects.all()

    return render(
        request, 'blog/post_detail.html',
        {
            'post': post,
            'categories' : categories,
            'tags' : tags,
        }
    )
