from django.conf.urls import url, include
from .views import (ProfileDetail, ProfileUpdate, PublicProfileDetail)

urlpatterns = [
    url(r'^profile/$',
        ProfileDetail.as_view(),
        name='profile'),
    url(r'^profile/edit/$',
        ProfileUpdate.as_view(),
        name='profile_update'),
    url(r'^profile/public/(?P<slug>[\w\-]+)/$',
        PublicProfileDetail.as_view(),
        name='public_profile'),
]