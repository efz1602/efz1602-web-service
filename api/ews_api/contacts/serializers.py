from rest_framework import serializers

from ews_api.contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['student_number', 'name', 'primary_phone', 'secondary_phone',
                  'city', 'country', 'field_or_industry', 'school_or_company',
                  'degree_or_job', 'other_info']
