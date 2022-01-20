from django.urls import path

from todos import views

app_name = 'todos'

urlpatterns = [
    path('', views.ListTodo.as_view(), name='todos'),
    path('<int:pk>/', views.DetailTodo.as_view(), name='todo'),
]