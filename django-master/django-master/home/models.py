from django.db import models


# Create your models here.
class EgModel(models.Model):
    string_field = models.CharField(max_length=100)
    textarea = models.TextField()
    integer = models.IntegerField()
    floating_number = models.FloatField()
    date_filed = models.DateField()
    image_filed = models.ImageField(upload_to="images")
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="images") 
    date = models.DateField()
    blogno = models.IntegerField(default=0)
    def __str__(self):
       return self.title
class comment(models.Model):
    address = models.CharField(max_length=100)   
    content = models.TextField()
    date = models.DateField()
    def __str__(self):
       return self.address
class contact(models.Model):
    address = models.CharField(max_length=100)   
    contactnum = models.BigIntegerField()
    def __str__(self):
       return self.contactnum