from rest_framework import generics, permissions
from django.contrib.auth.models import User
from . import serializers

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer
    permission_classes = [permissions.AllowAny]
