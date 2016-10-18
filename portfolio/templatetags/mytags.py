from django import template
from django.utils import timezone
from portfolio.models import Project, Post
register = template.Library()

@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)


# add tag for lates projects
@register.inclusion_tag('latest-projects.html')
def show_latest_projects(latest_projects):
    # fetch limited latest projects for the related sidebar widjet
    latest_projects = Project.objects.all().order_by('-end_date')[:6]

    return{
        'latest_projects': latest_projects,
    }



# add tag for latest posts
@register.inclusion_tag('latest-posts.html')
def show_latest_posts(latest_posts):
    # fetch latest posts list for sidebar and footer
    latest_posts = Post.published.filter(created__lte=timezone.now()).order_by('-created')[:3]

    return {
        'latest_posts' : latest_posts,
        }
