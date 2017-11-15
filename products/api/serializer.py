from rest_framework import serializers
from user.api.serializers import UserSerializer

from ..models import Product
##########################################################################


class PublicProductSerializer(serializers.ModelSerializer):
    """
    Serializer provides data for the public profile of a product
    does not show the email!
    """
    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Private product serializer. CUD products of user is owner.
    More fields will be sent to the user.
    """

    user = UserSerializer(read_only=True)

    class Meta:
        model = Product
        exclude = ('id',)
