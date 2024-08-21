from django.db import models
from accounts.models import ClubsModel
from django.contrib.auth.models import User
# Create your models here.


#Products
class ProductsClassificationModel(models.Model):
    title = models.CharField(max_length=254, null=True)
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")

class ProductsModel(models.Model):
    club = models.ForeignKey(ClubsModel, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=254, null=True)
    desc = models.TextField(null=True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    classification = models.ManyToManyField('ProductsClassificationModel')
    is_enabled = models.BooleanField(default=True)
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")

class ProductsImage(models.Model):
    product = models.ForeignKey('ProductsModel', on_delete=models.CASCADE)
    img = models.ImageField(upload_to="Products/imgs/%Y/%m/%d", blank=True, null=True)
    img_base64 = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")

class ProductsRate(models.Model):
    product = models.ForeignKey('ProductsModel', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    msg = models.TextField()
    rate = models.IntegerField()
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")





#Services
class ServicesClassificationModel(models.Model):
    title = models.CharField(max_length=254, null=True)
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")

class ServicesModel(models.Model):
    club = models.ForeignKey(ClubsModel, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=254, null=True)
    desc = models.TextField(null=True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    classification = models.ManyToManyField('ProductsClassificationModel')
    is_enabled = models.BooleanField(default=True)
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")

class ServicesImage(models.Model):
    product = models.ForeignKey('ServicesModel', on_delete=models.CASCADE)
    img = models.ImageField(upload_to="Services/imgs/%Y/%m/%d", blank=True, null=True)
    img_base64 = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")

class ServicesRate(models.Model):
    product = models.ForeignKey('ServicesModel', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    msg = models.TextField()
    rate = models.IntegerField()
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")



#Blog
class BlogClassificationModel(models.Model):
    title = models.CharField(max_length=254, null=True)
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")

class Blog(models.Model):
    title = models.CharField(max_length=254, null=True)
    img = models.ImageField(upload_to="blog/imgs/%Y/%m/%d", blank=True, null=True)
    body = models.TextField()
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")