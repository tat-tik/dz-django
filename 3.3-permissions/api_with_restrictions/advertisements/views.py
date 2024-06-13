from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api_with_restrictions.advertisements.models import Advertisement
from api_with_restrictions.advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description', 'status', 'creator', ]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return [IsAuthenticatedOrReadOnly(), IsOwner()]
