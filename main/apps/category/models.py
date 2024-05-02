from django.db import models
from ..common.models import BaseModel, BaseMeta
from ..common.utils import upload_images



class Category(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_images(path='category_images/'), null=True, blank=True)
    

    class Meta(BaseMeta):
        verbose_name = 'Category'
        verbose_name_plural = 'Categories' 

    def __str__(self):
        return self.title
    

