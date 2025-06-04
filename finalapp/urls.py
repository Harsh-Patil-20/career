from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('questionnaire/', views.questionnaire_view, name='questionnaire_form'),
    path('predict/', views.predict, name='predict'),
]
