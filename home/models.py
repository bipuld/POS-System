from django.db import models
from django.contrib.auth.models import User
# Create your models here.


from django.utils import timezone


class UserInfo(models.Model):
    GENDER_CHOOSE = (('male', 'Male'), ('female', 'Female'), ('other', 'Others'))
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="Inventory_User", primary_key=True)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOOSE, default="male")
    phone = models.CharField(max_length=255)
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.CharField(max_length=25)
    company_name = models.CharField(max_length=55)
    designation = models.CharField(max_length=155)
    country = models.CharField(max_length=15)
    address = models.CharField(max_length=55)
    phone.help_text = "if has more than one no write separated with comma."
    image = models.ImageField(upload_to="profile", blank=True, null=True)
    is_verify = models.BooleanField(default=False)
    intro = models.TextField(blank=True, null=True)
    email = models.EmailField()

    @property
    def full_name(self):
        if self.user:
            return f"{self.first_name} {self.last_name}"
        else:
            return None
    def __str__(self):
        if self.user:
            return f"{self.first_name} {self.last_name}"
        else:
            return "Anonymous User"




class Contact(models.Model):
    name = models.CharField(max_length=155, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    business_type = models.CharField(max_length=55)
    subject=  models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return f"{self.name} {self.email} {self.business_type}"
    
    