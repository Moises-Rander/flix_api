from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', views.ActorDetailUpdateDeleteView.as_view(), name='actor-detail-update-delete'),
]
