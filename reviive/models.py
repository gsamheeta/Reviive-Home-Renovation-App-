from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class RenovationPrice(models.Model):
    item = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    name = models.CharField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reviive:renovationPriceGuide')

# class RenovationPrice:
#     def __init__(self, renovid, item, price):
#         self.renovid = renovid
#         self.item = item
#         self.price = price
#
# renovation1 = RenovationPrice(renovid="1001", item= "Paint (Behr)", price="$50 per gallon")
# renovation2 = RenovationPrice(renovid="1002", item= "Paint (Sherwin-Williams)", price="$40 to $70 per gallon")
# renovation3 = RenovationPrice(renovid="1003", item= "Paint (Dulux)", price="$30 to $60 per gallon")
# renovation4 = RenovationPrice(renovid="1004", item= "Tiles (Mohawk)", price="$1 to $5 per square foot")
# renovation5 = RenovationPrice(renovid="1005", item= "Tiles (Marazzi)", price="$2 to $7 per square foot")
# renovation6 = RenovationPrice(renovid="1006", item= "Tiles (Porcelanosa)", price="$10 per square foot")
# renovation7 = RenovationPrice(renovid="1007", item= "Mirror (IKEA)", price="$10 to $100")
# renovation8 = RenovationPrice(renovid="1008", item= "Mirror (Pottery)", price="$100")
# renovation9 = RenovationPrice(renovid="1009", item= "Mirror (Barn)", price="$100 to $300")
#
# renovations = [renovation1, renovation2, renovation5, renovation9, renovation3, renovation7, renovation4, renovation6, renovation8]

# renovations = []

regular_user = {"username": "samheeta", "password": "regular"}
