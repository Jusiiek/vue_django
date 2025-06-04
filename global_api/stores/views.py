from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

from .models import Store
from .serializers import StoreSerializer

# Create your views here.
class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        if not request.user.is_global_user:
            return Response([], status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
