"""
Modelos del post
"""

from django.db import models


class Countries(models.Model):
    """Country Model"""

    country_name = models.CharField(max_length=3)

    




class User(models.Model):
    """User Model"""

    #Django adds default id to the class

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    bio = models.TextField(blank=True)


    is_admin = models.BooleanField(default=False)


    birthday = models.DateField(blank=True, null=True)

    # DateTime Almacena tambien la hora
    # cuando se crea 
    created_at = models.DateTimeField(auto_now_add=True)
    # cuando se modifica
    modified_at = models.DateTimeField(auto_now=True)
    
    city = models.CharField(max_length=100, default="NO REGISTERS")
    country = models.ForeignKey(Countries, on_delete="SET NULL", null=True)
