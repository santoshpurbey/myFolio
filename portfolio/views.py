from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import Http404
from django.shortcuts import render, redirect
from django.template.context import RequestContext
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Project, Skill, Category, ProjectImage, Post, PostLayout

def about(request):
    return render(request, 'about.html', {})


def portfolio_list(request):
    object_list = Project.objects.filter(end_date__lte=timezone.now()).order_by('-end_date')
    categories = Category.objects.all()

    # grub post layouts
    layouts = PostLayout.objects.all()

    # pagenation
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        projects = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver the last page of results
        projects = paginator.page(paginator.num_pages)

    return render(request, 'portfolio/portfolio_list.html',
                {
                    'projects': projects,
                    'categories': categories,
                    'page': page,
                    'layouts': layouts,
                })


def portfolio_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    project_images = ProjectImage.objects.filter(project__pk=pk)

    # grub Categories
    categories = Category.objects.all()

    # grub Skills
    skills = Skill.objects.all()

    return render(
        request,
        'portfolio/portfolio_detail.html',
        {
            'project': project,
            'skills': skills,
            'categories': categories,
            'project_images': project_images,
        }
    )


def contact(request):
    return render(request, 'contact.html', {})


def blog_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')

    # grub categories
    categories = Category.objects.all()

    # grub post layouts
    layouts = PostLayout.objects.all()


    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver the last page of results
        posts = paginator.page(paginator.num_pages)

    # fetch latest posts list for sidebar and footer
    latest_posts = Post.published.filter(created__lte=timezone.now()).order_by('-created')[:3]

    # fetch limited latest projects for the related sidebar widjet
    latest_projects = Project.objects.all().order_by('end_date')[:6]
    return render(request, 'blog/blog_list.html', {
        'posts': posts,
        'page' : page,
        'categories': categories,
        'layouts' : layouts,
        'latest_projects': latest_projects,
        'latest_posts' : latest_posts,
        })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # grub Categories
    categories = Category.objects.all()

    # grub Skills
    skills = Skill.objects.all()

    return render(
        request, 'blog/post_detail.html',
        {
            'post': post,
            'categories': categories,
            'skills': skills,
        }
    )


def comming_soon(request):
    return render(request, 'comming_soon.html', {})
