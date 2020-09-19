from django.urls import path

from . import views

urlpatterns = [
    path('image', views.FileUpload.as_view())
]
