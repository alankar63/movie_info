from django.http import HttpResponse
import movie_api

def hello(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index(request,movie):
    str=movie_api.get_data(movie)
    return HttpResponse(str)

