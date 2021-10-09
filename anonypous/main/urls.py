

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
    path('class', views.classpage, name='class'),
    path('assignment/student', views.studentassignment, name="studentassignment"),
    path('assignment/teacher', views.teacherassignment, name="teacherassignment")
]
