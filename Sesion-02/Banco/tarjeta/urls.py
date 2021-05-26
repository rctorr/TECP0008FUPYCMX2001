from django.urls import path
from . import views

# /
urlpatterns = [
	# URL /
	path('', views.index, name="index"),
]
