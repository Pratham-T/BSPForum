from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    #path('', views.indexView, name='home'),
    path('profile/<str:username>', views.ProfileView.profile, name='profile'),
    path('login/', LoginView.as_view(redirect_field_name='index'), name='login_url'),
    path('register/', views.registerView, name='register_url'),
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        # views.activateUser, name='activate'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]