from django.db import models
from ..common.models import BaseModel, BaseMeta
from ..category.models import Category
from ..common.utils import upload_images  


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    image = models.ImageField(upload_to=upload_images(path='product_images/'), null=True, blank=True)
    description = models.TextField()


    class Meta(BaseMeta):
        verbose_name = 'Product'
        verbose_name_plural = 'Products' 

    def __str__(self):
        return self.title
    

