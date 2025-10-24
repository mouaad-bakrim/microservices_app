# commandes/urls.py
from django.urls import path
from django.http import HttpResponse

def test(request):
    return HttpResponse("Service commandes OK")

urlpatterns = [
    path('', test, name='test_commandes'),
]
