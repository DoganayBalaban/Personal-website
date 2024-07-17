from django.shortcuts import render,redirect
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse
from .models import Bio,Blog,Technologies,Topic,Project,ProjectImages,Contact
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
    allBlog = Blog.objects.all()
    context = {
        "blogs":blogs,
        "allBlog":allBlog
    }
    return render(request,"base/blog-detail.html",context)


def portfolioView(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    projects = Project.objects.filter(
        Q(title__icontains=q) |
        Q(technologies__name__icontains=q)).distinct().order_by("-created_at")
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
    bio = Bio.objects.first()
    projects = Project.objects.all().order_by("-created_at")
    context = {
        'bio':bio,
        'projects':projects
    }
    return render(request,"base/aboutme.html",context)

def contactView(request):
    bio=Bio.objects.first()
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        from_email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name,email=from_email,surname=surname,message=message)
        if name and message and from_email:
             try:
                send_mail(name, message, from_email, ["balabandoganay@gmail.com"])
             except BadHeaderError:
                return HttpResponse("Invalid header found.")
        
        return redirect('contact')

    context = {
        'bio':bio
    }
    return render(request,'base/contact.html',context)
