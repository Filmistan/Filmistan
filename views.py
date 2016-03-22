from django.shortcuts import render
from .models import Film
from django.utils import timezone


# Create your views here.

def film_list(request):
    films = Film.objects.filter(createDate__lte=timezone.now()).order_by('createDate')
    return render(request, 'film/film_list.html', {'films': films})
