from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('portfolio/', views.portfolioView, name='portfolio'),
    path('blogs/', views.blogsView, name='blog'),
    path('blog/<int:id>/', views.blogDetailView, name='blog-detail'),
    path('ben/', views.meView, name='ben'),
    path('ulas/', views.contactView, name='contact'),
]
