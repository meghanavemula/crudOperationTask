
from django.urls import path
from .import views

urlpatterns = [
    path('',views.insert,name='create'),
    path('select/',views.select,name='select'),
    path('edit/<int:Id>',views.edit,name='edit'),
    path('delete/<int:Id>',views.delete,name='delete'),


]
