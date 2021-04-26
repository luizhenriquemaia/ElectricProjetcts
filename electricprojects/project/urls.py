from django.urls import path

from . import views


app_name = "project"

urlpatterns = [
    path('new-project/', views.new_project, name='new_project'),
]