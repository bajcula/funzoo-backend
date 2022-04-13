from accounts.serializers import CustomUserDetailsSerializer
from accounts.models import MyUser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = CustomUserDetailsSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated']
    ordering = ['-updated']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return MyUser.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = MyUser.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj