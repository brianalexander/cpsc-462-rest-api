from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from tictactoe.models import TicTacToe
from tictactoe.serializers import TicTacToeSerializer


# Create your views here.

class TicTacToeViewSet(ModelViewSet):
    queryset = TicTacToe.objects.all()
    serializer_class = TicTacToeSerializer
    permission_classes = [AllowAny]
