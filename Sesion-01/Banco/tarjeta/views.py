from django.shortcuts import render

# Create your views here.
def index(request):
	""" Atiende la petición GET / """
	return render(request, "tarjeta/index.html")