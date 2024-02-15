from django.urls import path

from . import views

app_name = "galleries"
urlpatterns = [
    path("", views.index),
    path("<int:gallery_id>", views.detail, name="detail")
]
