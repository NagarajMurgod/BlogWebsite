
from django.urls import path
from .views import ProfileView,ProfileApiView


urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('api/profiledata/',ProfileApiView.as_view())
    
]