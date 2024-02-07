from django.db import models
from django.contrib.auth.models import User
from flower.models import Flower
# Create your models here.
ORDER_STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, )
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=1)
    status = models.CharField(choices = ORDER_STATUS, max_length = 10, default = "Pending")
    # status = models.CharField(max_length = 10, default = "Pending")
    cancel = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.user.first_name} TITLE: {self.flower.title}"
    
    