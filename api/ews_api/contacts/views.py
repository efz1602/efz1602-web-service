# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from ews_api.contacts.models import Contact
from ews_api.contacts.permissions import IsOwnerOrReadOnly
from ews_api.contacts.serializers import ContactSerializer


class ContactViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
