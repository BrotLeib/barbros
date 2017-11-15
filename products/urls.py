from django.conf.urls import url, include
from .views import HomeView
from .views import ProductDetail, ProductCreate

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='organizer_home'),
    url(r'^create', ProductCreate.as_view(), name='product_create'),
    url(r'^find/(?P<slug>[\w]+)/$', ProductDetail.as_view(), name='product_detail'),
]
