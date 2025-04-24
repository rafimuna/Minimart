# users/serializers.py

from rest_framework import serializers
from .models import CustomUser

# ✅ Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password')

    def create(self, validated_data):
        # ইউজার তৈরি করার সময় password হ্যাশ করে সেট করা হচ্ছে
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
