from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('survey/<str:pk>', views.survey, name = 'survey'),
   # path('pregunta/<str:pk>', views.pregunta, name = 'pregunta'),
    path('vote/<str:pk>', views.vote, name = 'vote'),
    path('result/<str:pk>', views.result, name = 'result')
]