from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CHRISTO_HOME.urls')),
    path('login/', LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='home/logout.html'), name='logout'),
    path('user/', include('CHRISTO_USER.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
