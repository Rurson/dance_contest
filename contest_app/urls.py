from django.urls import path

from contest_app import views

app_name = 'contest'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('details/<int:pk>/', views.DetailsView.as_view(), name='details'),
    path('stage/<int:pk>/', views.StageView.as_view(), name='stage'),
    path('voting/<int:vote_id>/', views.vote, name='voting')

]
