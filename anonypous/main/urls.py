

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

    path('class/<str:classCode>/', views.classpage, name='class'),
    path('class/<classCode>/<str:assignmentCode>/', views.assignment, name="assignment"),
    path('class/<classCode>/<assignmentCode>/<str:docCode>/', views.submission, name='submission'),

    path('test', views.test, name='test'),
    path('classfail', views.classfail, name="classfail"),

]
