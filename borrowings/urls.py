from django.urls import path, include
from rest_framework.routers import DefaultRouter
from borrowings.views import BorrovingViewset

router = DefaultRouter()
router.register(r'', BorrovingViewset, basename="borrowing")

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/return/', BorrovingViewset.as_view({'post': 'return_book'}), name='book-return'),
]


app_name = "borrowings"