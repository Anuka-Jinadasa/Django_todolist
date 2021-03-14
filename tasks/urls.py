from django.urls import path
from . import views

urlpatterns = [

    path('',views.index , name = "list"),
    path('updateTask/<str:pk>/' , views.update, name="updateTask")
]
