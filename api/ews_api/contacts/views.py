# Create your views here.
from rest_framework import viewsets, permissions

from ews_api.contacts.models import Contact
from ews_api.contacts.serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
