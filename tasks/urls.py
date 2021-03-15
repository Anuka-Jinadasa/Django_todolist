from django.urls import path
from . import views

urlpatterns = [

    path('',views.index , name = "list"),
    path('updateTask/<str:pk>/' , views.update, name="updateTask"),
    path('deleteTask/<str:pk>/' , views.delete, name="deleteTask")
]
