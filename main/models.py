from django.db import models

# Create your models here.
class products(models.Model):
    CATEGORY =(
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door')
    )
    product_name = models.CharField(max_length=200, null=True)
    product_category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    product_price = models.FloatField(null=True)
    product_description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField("Date Created", auto_now_add =True, null=True)
    def __str__(self):
        return self.product_name
    
class customer(models.Model):
    customer_name = models.CharField(max_length=200, null=True)
    customer_phone = models.CharField(max_length=200, null=True)
    customer_email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField("Date Created", auto_now_add =True, null=True)
    def __str__(self):
        return self.customer_name

class Order(models.Model):
    STATUS =(
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivery', 'Delivery'),
    )
    #customer =
    #product =
    date_created = models.DateTimeField("Date Created", auto_now_add =True, null=True)
    status = models.CharField(max_length=200, null=True, choices = STATUS)