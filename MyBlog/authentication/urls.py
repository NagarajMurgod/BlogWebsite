from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('signup/', views.SignupView.as_view(), name='signup'),
    # path('signin/',views.SigninView.as_view(), name='signin'),
    path('logout/',LogoutView.as_view(next_page='/')),
    path('login/',views.LoginPage.as_view()),
    path('signup/',views.SignupPage.as_view())
]