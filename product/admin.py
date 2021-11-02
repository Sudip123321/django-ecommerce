from django.contrib import admin
from .models import (Product,
                    ImageUpload,
                    Category,
                    OrderItem,
                    ) 

admin.site.register(Product)
admin.site.register(ImageUpload)
admin.site.register(OrderItem)
admin.site.register(Category)
