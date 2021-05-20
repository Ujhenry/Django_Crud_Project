from django.urls import path
from django.urls.conf import include
from Blog import views
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdatedView, BlogDeleteView


urlpatterns =[
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdatedView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),

]