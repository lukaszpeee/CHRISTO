from django.urls import path

from CHRISTO_USER import views

urlpatterns = [
    path('home/', views.user_home, name='user_home'),
    path('profile/', views.user_profile, name='user_profile'),
    path('twitter_profiles_lists/', views.user_profile, name='user_twitter_profiles_lists'),
    path('twitter_profiles_list_details/', views.user_profile, name='user_twitter_profiles_list_details'),


]
