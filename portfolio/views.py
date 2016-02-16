from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from .models import Project


"""
def home(request):
    return  render( request, 'portfolio/home.html', {} )

def about(request):
    return render( request, 'portfolio/about.html', {} )

def portfolio_list(request):
    projects = Project.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
    return render(request, 'portfolio/portfolio_list.html', {'projects': projects})

def portfolio_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/portfolio_detail.html', {'project': project})

def contact(request):
    return render( request, 'portfolio/contact.html', {})
"""
