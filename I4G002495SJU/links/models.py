from django.db import models
from django.contrib.auth.models import User
from .managers import ActiveLinkManager


# Create your models here.
class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)  # 

    active = models.BooleanField(default=True)  # is this link active?

    objects = models.Manager()  # The default manager
    public = ActiveLinkManager()  # A custom manager

    def __str__(self):
        return self.identifier