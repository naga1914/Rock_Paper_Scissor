from django.urls import path
from . import views

urlpatterns = [
    path('', views.rps_game, name='rock_paper_scissor'),
]
