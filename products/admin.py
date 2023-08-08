from django.contrib import admin
from .models import ProductQuest, QuestComment

# Register your models here.
admin.site.register(ProductQuest)
admin.site.register(QuestComment)