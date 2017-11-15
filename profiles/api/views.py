from django.http import Http404

from rest_framework.views import APIView

from ..models import Profile
from .serializer import ProfileSerializer


from rest_framework import generics, permissions
from rest_framework.response import Response


####################################################################


class ProfileView(APIView):
    """
    Retrieve profile Information - only GET is allowed on this view
    """
    def get_object(self, request):
        try:
            return Profile.objects.get(user=request.user)
        # add prefetch and select prefetch to optimise database here
        # this to add database optimisation there is an formulated method here
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        profile = self.get_object(request)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)




