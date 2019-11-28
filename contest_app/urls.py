from django.urls import path

from contest_app import views

app_name = 'contest'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('details/<int:pk>', views.DetailsView.as_view(), name='details'),
    path('vote/<int:pk>', views.VoteView.as_view(), name='vote'),
    path('voting/<int:vote_id>', views.vote, name='voting')

]
