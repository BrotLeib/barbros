from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token

from profiles.api import views as profile_views
from user.api import views as user_views
from products.api import views as products_views



urlpatterns = [

    # products

    url(r'^products/(?P<pk>[0-9]+)/$', products_views.PrivateProductDetail.as_view()),
    url(r'^products/detail/(?P<key>[\w]{6})/$', products_views.PublicProductDetail.as_view()),

    # profile

    url(r'^profile/$', profile_views.ProfileView.as_view()),
    url(r'^profile/products/$', products_views.ProductsListView.as_view()),

    # user

    url(r'^users/$', user_views.UserList.as_view()),
    url(r'^users/create/$', user_views.UserCreate.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', user_views.UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/$', obtain_jwt_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
