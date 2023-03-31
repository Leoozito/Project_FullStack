from django.urls import path, include
from .views import RoomView

urlpatterns = [
    path('api/', RoomView.as_view())
]