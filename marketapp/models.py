from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
    )
    shops = models.ManyToManyField(
        'Shop',
        related_name='product_categories',
    )

    def __str__(self):
        return self.name


class ShopType(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
    )

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(
        max_length=128
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    shop_type = models.ForeignKey(
        'ShopType',
        on_delete=models.CASCADE,
    )
    width = models.CharField(
        max_length=64,
    )
    height = models.CharField(
        max_length=64,
    )
    sale_commission = models.FloatField(
        default=0,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(
        max_length=128,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    shop = models.ForeignKey(
        'Shop',
        on_delete=models.CASCADE,
    )
    product_category = models.ManyToManyField(
       'ProductCategory',
    )
    price = models.FloatField()
    photo = models.TextField(
        null=True,
        blank=True,
    )
    weight = models.FloatField(
        null=True,
    )
    key_words = models.TextField(
       null=True,
       blank=True,
    )

    def __str__(self):
        return self.product_name
