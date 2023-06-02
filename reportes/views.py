from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from .serializers import ReporteSerializer

from .models import Reporte


@api_view(['GET'])
def getReportes(request):
    reportes = Reporte.objects.all()
    serializer = ReporteSerializer(reportes, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def postReporte(request):
    data = request.data
    reporte = Reporte.objects.create(
        esp32 = data['esp32'],
        mensaje = data['mensaje'],
        fecha = data['fecha'],
        hora = data['hora'],
        latitud = data['latitud'],
        longitud = data['longitud']
    )
        
    serializer = ReporteSerializer(reporte, many = False)
    return Response(serializer.data)