from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    CURRENCIES = [
        ('USD', 'USD'),
        ('ARS', 'ARS'),
        # puedes añadir más monedas si lo necesitas
    ]
    currency = models.CharField(max_length=3, choices=CURRENCIES, default='USD')
