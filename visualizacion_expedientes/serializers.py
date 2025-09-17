# visualizacion_expedientes/serializers.py
from rest_framework import serializers
from gestdocu.models import TipoDocumento, Documento, Tiene
from accounts.models import User, Cliente

class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
    creado_por = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    expediente = serializers.PrimaryKeyRelatedField(queryset=TipoDocumento.objects.all())
    tipo = serializers.PrimaryKeyRelatedField(queryset=TipoDocumento.objects.all())

    class Meta:
        model = Documento
        fields = '__all__'

class TieneSerializer(serializers.ModelSerializer):
    caso = serializers.PrimaryKeyRelatedField(queryset=Tiene.caso.field.related_model.objects.all())  # Mejor práctica
    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())

    class Meta:
        model = Tiene
        fields = '__all__'