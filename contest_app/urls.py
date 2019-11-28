from django.urls import path

from contest_app import views

app_name='contest_app'
urlpatterns = [
    path('',views.IndexView.as_view(), name='index')
]
