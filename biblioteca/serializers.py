from rest_framework import serializers
from biblioteca.models import biblioteca, livraria

class bibliotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = biblioteca
        fields = '__all__'
    
class livrariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = livraria
        fields = '__all__'