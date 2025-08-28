from django.urls import path
from . import views

urlpatterns = [
    path('all_todos/', views.all_todos, name='all_todos'),
    path('new_todo/', views.new_todo, name='new_todo'),
    path('edit_todo/<int:id>/', views.edit_todo, name='edit_todo'),
    path('del_todo/<int:id>/', views.del_todo, name='del_todo'),
]
