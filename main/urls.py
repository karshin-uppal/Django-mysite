from django.urls import path
from . import views #. means current directory, so we are importing views.py from the current directory

urlpatterns = [
    path("<str:name>/", views.index, name = "index"),
]