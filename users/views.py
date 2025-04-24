# users/views.py

from rest_framework import generics
from .serializers import RegisterSerializer
from .models import CustomUser

# ✅ Register View: নতুন ইউজার রেজিস্ট্রেশন API
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
