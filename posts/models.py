"""
Modelos del post
"""

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """ Post Model """

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="posts/photos")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey("users.Profile", on_delete=models.CASCADE)

    def __str__(self):
        """ Return Title and username """
        return f'{self.title} by @{self.user}'
