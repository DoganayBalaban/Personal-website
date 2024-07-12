from django.shortcuts import render
from django.http import HttpResponse
from .models import Bio,Blog,Technologies,Topic
from django.db.models import Q

# Create your views here.
def homeView(request):
    bio = Bio.objects.first()
    blogs = Blog.objects.all()[:3]
    techs = Technologies.objects.all()[2:]
    context = {
        'bio':bio,
        'blogs':blogs,
        'techs':techs
    
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
    context = {
        "blogs":blogs
    }
    return render(request,"base/blog-detail.html",context)


def portfolioView(request):
    return HttpResponse("Portfolio")


def meView(request):
    return HttpResponse("Ben Kimim")

def contactView(request):
    return HttpResponse("Bana Ulaş")