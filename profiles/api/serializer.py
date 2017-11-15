from rest_framework import serializers
from ..models import Profile
from user.api.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):

    # user = serializers.ReadOnlyField(source='user.email')
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'