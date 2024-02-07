from django.db import models
from django.contrib.auth.models import User
from account.models import Seller
# Create your models here.
# ORDER_STATUS = [
#     ('Completed', 'Completed'),
#     ('Pending', 'Pending'),
#     ('Running', 'Running'),
# ]
class FlowerCategory(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    def __str__(self):
        return self.name
    
class Flower(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="flower/images/")
    quantity = models.PositiveIntegerField(default=1)
    # sales_count = models.PositiveIntegerField(default=0)
    category = models.ManyToManyField(FlowerCategory)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"