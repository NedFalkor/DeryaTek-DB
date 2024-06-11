from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, permissions, status, response

from dt_gigs.models.festival import Festival
from dt_gigs.serializers.festival_serializer import FestivalSerializer


class FestivalCRUD(viewsets.ModelViewSet):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer

    def get_permissions(self):
        """Assign permissions based on the action."""
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        """Customize creation of a Festival."""
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return response.Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """Customize updating of a Festival."""
        try:
            return super().update(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return response.Response({"error": "Festival not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        """Customize deletion of a Festival."""
        try:
            return super().destroy(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return response.Response({"error": "Festival not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        """List all festivals."""
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a single festival."""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)
