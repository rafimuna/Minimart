# product/models.py

from django.db import models

# ✅ ক্যাটাগরি মডেল (যদি প্রোডাক্টকে ক্যাটাগরি অনুযায়ী ভাগ করতে চাও)
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# ✅ মেইন প্রোডাক্ট মডেল
class Product(models.Model):
    title = models.CharField(max_length=200)  # প্রোডাক্টের নাম
    description = models.TextField()  # প্রোডাক্টের বর্ণনা
    price = models.DecimalField(max_digits=10, decimal_places=2)  # প্রোডাক্টের দাম
    stock = models.PositiveIntegerField()  # স্টক সংখ্যা
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # ক্যাটাগরি রিলেশন
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)  # ইমেজ আপলোড
    video = models.FileField(upload_to='product_videos/', null=True, blank=True)  # ভিডিও আপলোড
    created_at = models.DateTimeField(auto_now_add=True)  # কবে তৈরি হয়েছে

    def __str__(self):
        return self.title
