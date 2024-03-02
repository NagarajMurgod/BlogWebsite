from django.urls import path,include
from . import views


urlpatterns = [
    path('addBlog/',views.CreateBlog.as_view(),name='addblog'),
    path('api/getallblogs/', views.GetAllBlogsApiView.as_view()),
    path('api/get_categories/',views.GetCategories.as_view())
]