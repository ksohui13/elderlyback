from django.db import models
from mainshop.models import TimeStampModel
from accounts.models import User
from products.models import Product

class Cart(TimeStampModel):
    quantity = models.IntegerField(default=0)                           #수량
    user     = models.ForeignKey(User, on_delete=models.CASCADE)        #유저
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)     #상품
    option   = models.ForeignKey('Option', on_delete=models.CASCADE)    #옵션

    class Meta:
        db_table = 'carts'

class Option(TimeStampModel):
    option_name = models.CharField(max_length=50)                              #상품 옵션

    class Meta:
        db_table = 'options'