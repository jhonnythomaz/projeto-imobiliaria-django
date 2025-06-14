# paginas/views.py

from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse("<h1>Olá, Mundo! Esta é a minha primeira página com Django!</h1>")