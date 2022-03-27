from dataclasses import field, fields
from rest_framework import serializers
from .models import Form


class FormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Form
        fields = ['name', 'address', 'email', 'country', 'file']
