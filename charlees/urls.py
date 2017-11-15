from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from products import urls as products_urls
from user import urls as auth_urls
from profiles import urls as profile_urls
from core import urls as core_urls
from products import urls as products_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include(auth_urls, app_name='user', namespace='dj-auth')),
    url(r'^profile/', include(profile_urls)),
    url(r'^products/', include(products_urls)),
    url(r'^api/', include(core_urls)),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
