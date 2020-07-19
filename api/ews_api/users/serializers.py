from django.contrib.auth import get_user_model
from rest_framework import serializers

from ews_api.contacts.models import Contact

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    student_number = serializers.IntegerField(write_only=True,
                                              required=True,
                                              style={
                                                  "input_type": "password"
                                              })
    password = serializers.CharField(write_only=True,
                                     required=True,
                                     style={
                                         "input_type": "password"
                                     })
    password_confirm = serializers.CharField(write_only=True,
                                             label="Confirm password",
                                             style={
                                                 "input_type": "password"
                                             })

    class Meta:
        model = User
        fields = [
            "student_number",
            "username",
            "password",
            "password_confirm",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        student_number = validated_data["student_number"]
        username = validated_data["username"]
        password = validated_data["password"]
        password_confirm = validated_data["password_confirm"]
        if not Contact.objects.filter(pk=student_number, name=username).exists():
            # only allow members in contacts
            raise serializers.ValidationError({"error": "Not allowed to register."})
        if password != password_confirm:
            raise serializers.ValidationError({"error": "Passwords don't match."})
        contact = Contact.objects.get(pk=student_number)
        user = User(username=username)
        user.set_password(password)
        user.save()
        # TODO: is there an atomicity issue?
        contact.owner = user
        contact.save()
        return user
