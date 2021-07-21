from django.urls import path
from .views import index, cadastro, delete_times

urlpatterns = [
    path('', index, name='index'),
    path('cadastro', cadastro, name='cadastro'),
    path('delete/<int:id>/', delete_times, name="delete_times") 

]