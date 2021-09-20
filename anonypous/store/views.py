from django.http.response import HttpResponse
from django.shortcuts import render




# Create your views here.
def root(request):
    return render(request, 'store/root.html', {})



