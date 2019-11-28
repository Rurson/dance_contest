from django.urls import path

from contest_app import views

app_name = 'contest'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('details/<pk>', views.DetailsView.as_view(), name='details'),
    path('vote/<pk>', views.VoteView.as_view(), name='vote')
]
