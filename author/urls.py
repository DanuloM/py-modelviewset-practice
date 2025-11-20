# Create your urls here
from django.urls import path, include
from rest_framework import routers

from author import views

router = routers.DefaultRouter()

router.register("authors", views.AuthorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
