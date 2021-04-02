from django.contrib import admin
from .models import Pizza, Topping, Customer

admin.site.register(Customer)
# admin.site.register(Menu)
admin.site.register(Pizza)
admin.site.register(Topping)

