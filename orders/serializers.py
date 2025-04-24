from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # user.username দেখাবে
    product = serializers.StringRelatedField()             # product.name দেখাবে

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['id', 'user', 'ordered_at']
