from django.db import models


# Create your models here.

class Banner(models.Model):
    img = models.CharField(max_length=200)
    alt_text = models.CharField(max_length=200, blank=True, null=True)


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'


class Marca(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=100,)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=400)
    image = models.ImageField(upload_to='product', blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.product.title

    class Meta:
        db_table = 'product_attribute'
