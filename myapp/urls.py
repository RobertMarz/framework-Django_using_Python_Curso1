from django.urls import path
#from myapp.views import hello #importado mi proyecto
from .import views #importado mi proyecto


urlpatterns = [
    path('',views.index), #192.168.100.62
    path('about/',views.about),
    #path('hello/<str:username>',views.hello) # str:username por int:id
    path('hello/<str:username>',views.hello),
    path('projects/',views.project),
    path('tasks/<int:id>',views.tasks),
    
       
]
    