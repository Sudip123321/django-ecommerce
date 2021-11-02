from django.core import validators
from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from django.contrib.auth.models import AbstractUser,Group


class User(AbstractUser):
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, unique=True)

    REQUIRED_FIELDS = ['groups_id', 'email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username



class ImageUpload(models.Model):
    file = models.FileField(default=None,blank=False,null=False,validators=[FileExtensionValidator(allowed_extensions=['jpg','png'])])

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        # return '%d: %s' %(self.id,self.title)
        return '%d: %s' % (self.id, self.title)

class Product(models.Model):
    product_tag  =  models.CharField(max_length=10)
    name =  models.CharField(max_length=100)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    stock = models.IntegerField()
    quantity = models.IntegerField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    image = models.JSONField(blank=True,null=True)
    discount = models.FloatField(null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.product_tag}{self.name}'

    def get_absolute_url(self):
        return reverse("product:products", kwargs={"slug": self.slug})
    

class OrderItem(models.Model):
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product,related_name="orderitem",on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    
    def get_total_product_price(self):
        return self.quantity*self.product.price

    def get_total_discount_product_price(self):
        return self.quantity * self.product.discount
    
    def get_amount_saved(self):
        return self.get_total_product_price() - self.get_total_discount_product_price()
    
    def get_final_price(self):
        if self.product.discount:
            return self.get_total_discount_product_price()
        return self.get_total_discount_product_price()


