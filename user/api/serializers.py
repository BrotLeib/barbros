from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from products.models import Product

user_model = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = user_model
        fields = ('email', 'products')