from django.urls import path
from . import views

urlpatterns =[
    path('test/',views.index,name='index'),
    path('show_question',views.question,name='question'),
    path('choice/<int:id_question>/',views.choice,name='choice'),
    path('results/<int:id_question>/',views.result,name='result')
]