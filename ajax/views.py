from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def home(request):
    return render(request, 'ajax/index.html')

def json(request):
    l=[x for x in range(10)]
    #return JsonResponse({"h1":'<h1>home</h1>','car':'farari'})
    return JsonResponse({"h1":l})