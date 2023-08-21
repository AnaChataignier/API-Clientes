from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf': "CPF inválido"})
        
        if not validate_nome(data['nome']):
            raise serializers.ValidationError({'nome': 'Não inclua números nesse campo'})
            
        if validate_rg(data['rg']):
            raise serializers.ValidationError({'rg': 'O RG deve conter 9 dígitos'})
            
        if not validate_celular(data['celular']):
            raise serializers.ValidationError({'celular':"O número deve seguir esse modelo: 21 91234-1234 (respeitando os espaços e traço)" })
                
        return data
  
    
        