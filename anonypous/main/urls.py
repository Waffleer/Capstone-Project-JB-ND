

from django.urls import path
from . import views


app_name = 'dashboard'

urlpatterns = [
    path('', views.root, name='Root'),
    path('dashboard', views.dashboard, name='Dashboard'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('register', views.register, name='register'),
    path('profile', views.profiles, name='profile'),
    path('invalid', views.invalid, name='invalid'),
    path('class/<str:classCode>/', views.classpage, name='class'),
    path('class/<classCode>/<str:assignmentCode>/', views.assignment, name="assignment"),
    path('class/<classCode>/<str:assignmentCode>/r/result', views.results, name='result'),
    path('class/<classCode>/<assignmentCode>/<str:docCode>/', views.grade, name='Grade'),


    path('test', views.test, name='test'),

]
