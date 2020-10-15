from django.shortcuts import render
# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Eoi,Empresa
from .serializers import EoiSerializer,EmpresaSerializer
from rest_framework import generics


from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class EoiViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
       `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.

    """
    
    queryset = Eoi.objects.all()
    serializer_class = EoiSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        eoi = self.get_object()
        return Response(eoi.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

 
class EmpresaViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
       `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.

    """
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        empresa = self.get_object()
        return Response(empresa.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)