from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from ckeditor.fields import RichTextField

fs = FileSystemStorage(location='/tmp')
blogimage = FileSystemStorage(location='/tmp')


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Articles(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField()
    description = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
