from django.db import models


# Choices created for users to be displayed options
categories = (('Highend', 'High Range'), ('Middle', 'Mid Range'))
Watches_For = (('MEN', 'Men'), ('WOMEN', 'Women'), ('CHILDREN', 'Children'))
ProductStatus = (('IN_STOCK', 'In Stock'), ('OUT_OF_STOCK', 'Out of Stock'))
rating = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))


class Category(models.Model):
    """
    Modal for categories
    """

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.name


class ProductStatus(models.Model):
    """
    Modal for product status
    """

    class Meta:
        verbose_name_plural = "Product Status"

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Modal for product
    """

    category = models.CharField(max_length=20, choices=categories, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    brand = models.CharField(max_length=254)
    description = models.TextField()
    features = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=3)
    rating = models.DecimalField(
                                 choices=rating,
                                 max_digits=6,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(
                              upload_to="products_images/",
                              null=True,
                              blank=True)

    def __str__(self):
        return self.name
