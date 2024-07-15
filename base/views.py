from django.shortcuts import render
from django.http import HttpResponse
from .models import Bio,Blog,Technologies,Topic,Project,ProjectImages
from django.db.models import Q

# Create your views here.
def homeView(request):
    bio = Bio.objects.first()
    blogs = Blog.objects.all()[:3]
    techs = Technologies.objects.all()[2:]
    projectImages = ProjectImages.objects.all()
    context = {
        'bio':bio,
        'blogs':blogs,
        'techs':techs,
        'projectImages':projectImages,
    
    }
    return render(request,'base/home.html',context)


def blogsView(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    blogs = Blog.objects.filter(
        Q(title__icontains=q) |
        Q(topic__name__icontains=q)
                                )
    topics = Topic.objects.all()

    context = {
        'blogs':blogs,
        'topics':topics
        }
    return render(request,'base/blogs.html',context)

def blogDetailView(request,id):
    blogs = Blog.objects.get(id=id)
    allBlog = Blog.objects.all();
    context = {
        "blogs":blogs,
        "allBlog":allBlog
    }
    return render(request,"base/blog-detail.html",context)


def portfolioView(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    projects = Project.objects.filter(
        Q(title__icontains=q) |
        Q(technologies__name__icontains=q)).distinct()
    technologies = Technologies.objects.all()
    context = {
        'projects':projects,
        'technologies':technologies,
    }
    return render(request,"base/porfolio.html",context)

def portfolioDetailView(request,id):
    project = Project.objects.get(id=id)
    technologies = Technologies.objects.all()
    images = ProjectImages.objects.filter(project=project)
    context = {
        'project':project,
        'technologies':technologies,
        'images':images
    }
    return render(request,"base/portfolio-detail.html",context)

def meView(request):
    context = {}
    return render(request,"base/aboutme.html",context)

def contactView(request):
    return HttpResponse("Bana Ulaş")