from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tictactoe import views

router = DefaultRouter()
router.register('', views.TicTacToeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
