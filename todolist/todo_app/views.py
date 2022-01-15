from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)
		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messages.success(request, ('Se agregó una actividad a la lista!'))
			return render(request, 'home.html', {'all_items': all_items})
	else:
		all_items = List.objects.all
		return render(request, "home.html", {'all_items': all_items})

def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ('La actividad se ha eliminado!'))
	return redirect('home')

def cross(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('home')

def uncross(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('home')