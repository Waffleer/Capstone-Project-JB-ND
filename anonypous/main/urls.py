

from django.urls import path
from . import views


app_name = 'dashboard'

urlpatterns = [
    path('dashboard', views.dashboard, name='Dashboard'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('register', views.register, name='register'),
    path('register/student', views.studentRegister, name='student'),
    path('register/teacher', views.teacherRegister, name='teacher'),
]