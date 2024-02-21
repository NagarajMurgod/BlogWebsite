
from django.urls import path,include
from .views import Homeview ,TestView


urlpatterns = [
    path('', Homeview.as_view()),
    path('test/', TestView.as_view())
]
