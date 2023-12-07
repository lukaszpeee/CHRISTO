from django.urls import path

from CHRISTO_USER import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('user_home/', views.user_home, name='user_home'),
]
