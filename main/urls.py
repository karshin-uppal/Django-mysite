from django.urls import path
from . import views #. means current directory, so we are importing views.py from the current directory

urlpatterns = [
    path("<int:id>/", views.index, name = "index"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create")
]