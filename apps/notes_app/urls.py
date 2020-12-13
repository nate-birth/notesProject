from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create_note', views.note, name="notes"),
    path('add_desc', views.description, name="add_description"),
    path('update_desc', views.update, name="update"),
    path('delete', views.delete, name="delete"),
]