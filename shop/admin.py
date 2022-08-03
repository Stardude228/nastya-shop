from django.contrib import admin

from .models import Category, Comment, Product, Like, Rating

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Product)
admin.site.register(Like)
admin.site.register(Rating)
