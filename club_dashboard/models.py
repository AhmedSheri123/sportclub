from django.db import models
from students.models import ProductsModel
# Create your models here.


class ProductsStockModel(models.Model):
    product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")
