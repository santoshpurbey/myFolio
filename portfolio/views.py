from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.context import RequestContext
from django.utils import timezone
from .models import Project, Skill, Category

def about(request):
    return render( request, 'about.html', {} )

def portfolio_list(request):
    projects = Project.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
    return render(request, 'portfolio_list.html', {'projects': projects})

def portfolio_detail(request, pk):
    project = Project.objects.get(pk=pk)
    skills = Skill.objects.filter(project__pk=pk)
    categories = Category.objects.filter(project__pk=pk)

    return render(
        request,
        'portfolio/portfolio_detail.html',
        {
            'project': project,
            'skills': skills,
            'categories': categories,
        }
    )

def contact(request):
    return render( request, 'contact.html', {})
