from django.urls import path


from user import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.UserView.as_view(), name='index')
]
