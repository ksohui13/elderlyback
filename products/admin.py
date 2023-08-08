from django.contrib import admin
from .models import Product, ProductQuest, QuestComment

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductQuest)
admin.site.register(QuestComment)