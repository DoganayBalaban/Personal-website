from django.db import models

# Create your models here.

class Bio(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100,default="N/A")
    bio = models.TextField()
    school = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='images/')
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    linkedin = models.URLField(max_length=100)
    github = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Topic(models.Model):
      name = models.CharField(max_length=200)
      def __str__(self):
            return self.name
      
class Technologies(models.Model):
         name = models.CharField(max_length=200)
         def __str__(self):
            return self.name
     

class Blog(models.Model):
    title = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null = True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Project(models.Model):
     title = models.CharField(max_length=100)
     miniDesc = models.TextField()
     description = models.TextField()
     technologies = models.ManyToManyField(Technologies,null = True,default="N/A")
     url = models.URLField(max_length=100)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
    
class ProjectImages(models.Model):
     project = models.ForeignKey(Project,related_name="images",on_delete=models.CASCADE)
     image = models.ImageField(upload_to='images/')
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
        return f"{self.project.title} Image"
     
    
class Contact(models.Model):
     name = models.CharField(max_length=100)
     surname = models.CharField(max_length=100)
     email = models.EmailField()
     message = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

