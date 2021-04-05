from django.db import models
from django.urls import reverse

class Pizza(models.Model):
    name = models.CharField(max_length = 120)
    # photo = models.ImageField(upload_to='images/', default='defo')

    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.OneToOneField(Pizza, on_delete = models.CASCADE, default = False)
    cheese = models.BooleanField(default = False, verbose_name = "Extra Cheese")
    onion = models.BooleanField(default = False, verbose_name = "Extra onion")
    tomato = models.BooleanField(default = False, verbose_name = "Extra tomato")
    quantity = models.PositiveIntegerField(default = 1)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.CharField(max_length = 2083, blank = True)
    # photo = models.ImageField(upload_to='images/', default='defo')

    def __str__(self):
        return str(self.pizza)

    def get_absolute_url(self):
        return reverse('detail', args = [str(self.id)])

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=16)
    email = models.CharField(max_length=64)
    phone_no = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.username}({self.customer_id})"

