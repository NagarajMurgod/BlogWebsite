from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('signup/', views.SignupView.as_view(), name='signup'),
    # path('signin/',views.SigninView.as_view(), name='signin'),
    path('logout/',LogoutView.as_view(next_page='/'), name='logout'),
    path('login/',views.LoginUserView.as_view(),name='login'),
    path('signup/',views.SignupPage.as_view())
]