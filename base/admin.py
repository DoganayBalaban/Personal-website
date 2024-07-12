from django.contrib import admin
from .models import Bio,Blog,Technologies,Topic,Project
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)

class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
admin.site.register(Bio)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Technologies)
admin.site.register(Topic)
admin.site.register(Project,ProjectAdmin)