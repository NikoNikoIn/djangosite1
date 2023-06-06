from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from blog.views import (
    blog_post_create_view,
)
from .views import (
    home_page,
    about_page,
    contact_page,
    example_page
)
from searches.views import search_view

urlpatterns = [
    path('', home_page),
    path('about/', about_page),
    path('blog-new/', blog_post_create_view),
    path('blog/', include('blog.urls')),
    path('example/', example_page),
    path('contact/', contact_page),
    path('admin/', admin.site.urls),
    path('search/', search_view),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)