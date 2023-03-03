from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.exceptions import ValidationError
# Create your models here.
def cin_valid(val):
    if len(val) !=8 :
        raise ValidationError("la longeur de cin doit être égale 8")
    return val
def email_valid(v):
    if str(v).endswith('@esprit.tn') == False:
        raise ValidationError('Votre email est invalide et doit se terminer par @esprit.tn')
    return v
class Person(AbstractUser):
    cin =models.CharField(primary_key=True,max_length=8, validators=[cin_valid])
    email = models.EmailField(unique=True, validators=[email_valid])
    username = models.CharField(unique=True,max_length=40)
    USERNAME_FIELD ='username'
    def __str__(self):
        return f"the person username is {self.username}"
    class Meta:
        verbose_name =('Person')
        verbose_name_plural ='Persons' 
    
    