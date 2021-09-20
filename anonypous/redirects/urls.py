



from django.urls import path
from . import views


app_name = 'redirects'

urlpatterns = [
    path('', views.root, name='Redirect')

]