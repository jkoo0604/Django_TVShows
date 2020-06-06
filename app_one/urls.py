from django.urls import path
from . import views

urlpatterns = [
    path('', views.gotoshows),
    path('shows', views.index),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<int:showid>', views.show),
    path('shows/<int:showid>/edit', views.edit),
    path('shows/<int:showid>/update', views.update),
    path('shows/<int:showid>/delete', views.delete),
    path('shows/ajax/validate', views.testunique, name="TestUnique")
]