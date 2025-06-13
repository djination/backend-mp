from rest_framework import status
from rest_framework.response import Response

class NoDeleteMixin:
    def destroy(self, request, *args, **kwargs):
        return Response({'detail': 'Delete not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)