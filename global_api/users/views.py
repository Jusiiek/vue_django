from django.views.generic import ListView

from rest_framework.response import Response
from rest_framework import status, permissions, viewsets
from django.shortcuts import get_object_or_404

from .models import User
from .serializers import UserSerializer


# Create your views here.
class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        serializer = UserSerializer(self.queryset, many=True)
        context['users'] = serializer.data
        return context


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        if not request.user.is_global_user:
            return Response([], status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        if pk == 'me':
            user = request.user
        else:
            user = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
