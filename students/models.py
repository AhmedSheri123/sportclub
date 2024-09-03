from django.db import models
from accounts.models import ClubsModel
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


#Products
class ProductsClassificationModel(models.Model):
    club = models.ForeignKey(ClubsModel, on_delete=models.CASCADE, null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=254, null=True)
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")

class ProductsModel(models.Model):
    club = models.ForeignKey(ClubsModel, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=254, null=True)
    desc = models.TextField(null=True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    stock = models.IntegerField(default=1, null=True)
    classification = models.ManyToManyField('ProductsClassificationModel', blank=True)
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
    club = models.ForeignKey(ClubsModel, on_delete=models.CASCADE, null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=254, null=True)
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")

    def __str__(self):
        return self.title


class ServicesModel(models.Model):
    club = models.ForeignKey(ClubsModel, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=254, null=True)
    desc = models.TextField(null=True)
    subscription_days = models.IntegerField(default=30, null=True)
    age_from = models.IntegerField()
    age_to = models.IntegerField()

    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    classification = models.ManyToManyField('ServicesClassificationModel', blank=True)
    is_enabled = models.BooleanField(default=True)
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")
    def __str__(self):
        return self.title

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
    club = models.ForeignKey(ClubsModel, on_delete=models.CASCADE, null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=254, null=True)
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")

class Blog(models.Model):
    club = models.ForeignKey(ClubsModel, on_delete=models.CASCADE, null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=254, null=True)
    desc = models.CharField(max_length=254, null=True)
    img = models.ImageField(upload_to="blog/imgs/%Y/%m/%d", blank=True, null=True)
    body = models.TextField()

    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")



class ServiceOrderModel(models.Model):
    service = models.ForeignKey(ServicesModel, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    is_complited = models.BooleanField(default=False)
    end_datetime = models.DateTimeField()
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")

    def has_subscription(self):
        if self.end_datetime > timezone.now():
            return True
        return False