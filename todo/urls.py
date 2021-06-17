from django.contrib import admin
from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.IndexView.as_view(), name='todolist'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name="todolist_detail"),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name="todolist_delete"),
    path('update/<int:pk>/', views.UpdateView.as_view(), name="todolist_update"),
    path('create/', views.TodoCreate, name="todolist_create"),
]