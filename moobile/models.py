from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(verbose_name = "Название",unique = True,max_length = 100)


    def __str__(self):
        return self.name



class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(verbose_name='Изображение')
    is_published = models.BooleanField(default=True)
    content = models.TextField(verbose_name='контент')
    date = models.DateTimeField(verbose_name='дата добавление', auto_now_add=True)
    category = models.ForeignKey(Category,on_delete = models.PROTECT,related_name = "product",verbose_name='Категория')
    tags = models.ManyToManyField(Tag, related_name = "productstag",verbose_name="Теги",blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='автор')
    def __str__(self):
        return f'{self.title} - {self.price}'
    

# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, verbose_name="Продукт",related_name = "images" ,on_delete=models.CASCADE)
#     image = models.ImageField(verbose_name="Изображение",upload_to='mob_images/', null=True)


    # def __str__(self):
    #     return f'Изображение для продукта: {self.product.title}'
    

class ProductAttribute(models.Model):
    class Meta:
        verbose_name = "атрибут:"
        verbose_name_plural = 'атрибуты:'


    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='attributes')
    key = models.CharField(verbose_name='ключ', max_length=100)
    value = models.CharField(verbose_name='значение', max_length=100)
    
    def __str__(self):
        return f'{self.key} - {self.value}'

