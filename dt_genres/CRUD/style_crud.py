from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from dt_genres.models.style import Style
from dt_genres.serializers.style_serializer import StyleSerializer


class StyleCRUD(viewsets.ModelViewSet):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        """Customize creation of a Style."""
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """Customize updating of a Style."""
        try:
            return super().update(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return Response({"error": "Style not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        """Customize deletion of a Style."""
        try:
            return super().destroy(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return Response({"error": "Style not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        """List all styles."""
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a single style."""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
