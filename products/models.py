from django.db import models


# Choices created for users to be displayed options

Watches_For = (('MEN', 'Men'), ('WOMEN', 'Women'), ('CHILDREN', 'Children'))
ProductStatus = (('IN_STOCK', 'In Stock'), ('OUT_OF_STOCK', 'Out of Stock'))
rating = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))

class Category(models.Model):
    """
    Model for Categories
    """

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class WatchesFor(models.Model):
    """
    Model for WatchesFor
    """

    class Meta:
        verbose_name_plural = "WatchesFor"

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ProductStatus(models.Model):
    """
    Model for Product Status
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

    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)
    Watches_For = models.ForeignKey("WatchesFor", choices=Watches_For, null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    brand = models.CharField(max_length=254)
    description = models.TextField()
    features = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
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
    product_status = models.ForeignKey("ProductStatus", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
