from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    description = models.TextField(max_length=600)
    available = models.BooleanField(default=True)
    stock = models.IntegerField()
    image1 = models.FileField(upload_to='product_pics',blank=True,null=True)
    image2 = models.FileField(upload_to='product_pics',blank=True,null=True)
    image3 = models.FileField(upload_to='product_pics',blank=True,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-create_at',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __str__(self):
        return self.name
    

    
