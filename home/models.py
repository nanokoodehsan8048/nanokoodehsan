from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('humic', 'کود هیومیک اسید'),
        ('apartment', 'گیاهان آپارتمانی'),
    ]
    
    name = models.CharField(max_length=200, verbose_name='نام محصول')
    description = models.TextField(verbose_name='توضیحات')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت')
    image = models.ImageField(upload_to='products/', verbose_name='تصویر')
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        verbose_name='دسته‌بندی'
    )
    
    def __str__(self):
        return self.name