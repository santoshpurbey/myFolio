from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import Http404
from django.shortcuts import render, redirect
from django.template.context import RequestContext
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import CommentForm
from .models import Project, Skill, Category, ProjectImage, Post, Comment


def about(request):
    return render(request, 'about.html', {})


def portfolio_list(request):
    projects = Project.objects.filter(end_date__lte=timezone.now()).order_by('end_date')
    categories = Category.objects.all()

    return render(request, 'portfolio/portfolio_list.html',
                {
                    'projects': projects,
                    'categories': categories

                })


def portfolio_detail(request, pk):
    project = Project.objects.get(pk=pk)
    skills = Skill.objects.filter(project__pk=pk)
    # categories = Category.objects.filter(project__pk=pk)
    project_images = ProjectImage.objects.filter(project__pk=pk)

    return render(
        request,
        'portfolio/portfolio_detail.html',
        {
            'project': project,
            'skills': skills,
            #'categories': categories,
            'project_images': project_images
        }
    )


def contact(request):
    return render(request, 'contact.html', {})


def blog_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    # grub categories
    categories = Category.objects.all()


    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver the last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/blog_list.html', {
        'posts': posts,
        'page' : page,
        'categories': categories,
        })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # grub categories
    categories = Category.objects.all()

    # Comments

    # List of active comments for this post
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create comment object but dont save it to db yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to this comment
            new_comment.post = post
            # save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request, 'blog/post_detail.html',
        {
            'post': post,
            'categories': categories,
            'comments': comments,
            'comment_form': comment_form,
        }
    )
