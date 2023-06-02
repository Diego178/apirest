from rest_framework.serializers import ModelSerializer
from .models import Reporte


class ReporteSerializer(ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'