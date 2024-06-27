#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# este nos permite mostrar como string
from .models import Project, Task 
# con ctrl espace veo los modelos, aqui puedo hacer consultas
from django.shortcuts import get_object_or_404
 
# Create your views here.
def index(request):
    return HttpResponse("index page")


def hello(request,username): #aqui agregamos el nuevo parametro username
    # print(type(id)) # esto lo vemos por consola
    # result = 100**id
    return HttpResponse("<h1> Hello %s</h1>" % username) # ahora sustituimos username por id
    #return HttpResponse("<h1> Hello %s</h1>" % id)


def about(request):
    return HttpResponse("about")


def project(request):
    # projects = Project.objects.all() #Nos devuelve una lista de proyectos y lo mentemos en una variable
    projects = list(Project.objects.values()) # lo convertimos en lista para poder serializarlo
    return JsonResponse(projects,safe = False) # ya no es 'projects' string es como lista
 

def tasks(request,id):
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task,id=id)
    return  HttpResponse('task: %s ' % task.title)
    #return  HttpResponse('tasks')


  