from rest_framework import viewsets
from .models import biblioteca, livraria
from .serializers import bibliotecaSerializer, livrariaSerializer

# Create your views here.

class bibliotecaViewSet(viewsets.ModelViewSet):
    queryset = biblioteca.objects.all()
    serializer_class = bibliotecaSerializer
    
class livrariaViewSet(viewsets.ModelViewSet):
    queryset = livraria.objects.all()
    serializer_class = livrariaSerializer