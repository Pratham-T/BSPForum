from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.PostView.as_view(), name='post'),
    path('search/', views.SearchResults, name='search'),
    path('new_post/', views.newPost, name='new_post'),
    path('<int:pk>/comment', views.newComment, name='new_comment'),
]