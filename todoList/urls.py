from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="list"),
	path('update/', views.update, name="update"),
	path('delete/', views.delete, name="delete"),
]	