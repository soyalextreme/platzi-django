"""
Modelos del post
"""

from django.db import models



class User(models.Model):
    """User Model"""

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    bio = models.TextField(blank=True)


    birthday = models.DateField(blank=True, null=True)

    # DateTime Almacena tambien la hora
    # cuando se crea 
    created_at = models.DateTimeField(auto_now_add=True)
    # cuando se modifica
    modified_at = models.DateTimeField(auto_now=True)
