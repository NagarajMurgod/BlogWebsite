from django.urls import path,include
from . import views
from blog.api import api_views


urlpatterns = [
    path('addBlog/',views.CreateBlog.as_view(),name='addblog'),
    path('updateBlog/<slug:pk>/',views.UpdateBlogView.as_view(), name = "update_blog"),
    path('api/getallblogs/', views.GetAllBlogsApiView.as_view()),
    path('api/get_categories/',views.GetCategories.as_view()),
    path('api/tag/<category>/',api_views.CategoryBLogApiView.as_view()),
    path('show/<category>/',views.DisplayCategoryBlogView.as_view(),name = "category_blogs"),
    path('<slug:slug>/', views.DisplayBlog.as_view(),name="display_blog"),
    path('api/filterBlogs/<int:id>/',views.FilterBLogApiView.as_view()),
    
    
]