from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('questionnaire/', views.questionnaire_view, name='questionnaire_form'),
    path('predict/', views.predict, name='predict'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
