from django.urls import path, include
from rest_framework.routers import DefaultRouter
from borrowings.views import BookViewset

router = DefaultRouter()
router.register(r'', BookViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/return/', BookViewset.as_view({'post': 'return_book'}), name='book-return'),
]


app_name = "borrowings"