from django.urls import path, include
from rest_framework import routers

from books.views import BookViewSet

router = routers.DefaultRouter()
router.register(r"", BookViewSet, basename="book")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "books"
