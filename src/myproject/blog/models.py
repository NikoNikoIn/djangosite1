from django.db import models
from django.conf import settings
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User


User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)
    def search(self, query):
        return self.filter(title__iexact = query)
    


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using = self.db)
    def published(self):
        return self.get_queryset().published()
    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)

class BlogPost(models.Model):
    user = models.ForeignKey(User, default = 1, on_delete = models.CASCADE)
    title = models.TextField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField(null = True, blank = True)
    publish_date = models.DateTimeField(auto_now = False, auto_now_add = False, blank = True, null = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to="image/", blank=True, null=True)

    objects = BlogPostManager()

    class Meta:
        ordering = ["-publish_date", "-updated", "-timestamp"]

    def get_absolute_url(self):
        return f"/blog/{self.slug}"
    

    def get_edit_url(self):
        return f"/blog/{self.slug}/edit"
    

    def get_delete_url(self):
        return f"/blog/{self.slug}/delete"
    
    def search(self, query):
        return self.filter(title__iexact = query)