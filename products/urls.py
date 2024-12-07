from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("read/<int:id>/", views.read, name="read"),
    path("update/<int:id>/", views.update, name="update"),
    path("delete/<int:id>/", views.delete, name="delete"),
]
