from django.urls import path
from django.contrib.auth import views as auth_view

from user import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),

]
