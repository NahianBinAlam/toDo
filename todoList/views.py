from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):

	context = {}
	return render(request, 'todoList/list.html', context)

def update(request):

	context = {}
	return render(request, 'todoList/update.html', context)

def delete(request):

	context = {}
	return render(request, 'todoList/delete.html', context)