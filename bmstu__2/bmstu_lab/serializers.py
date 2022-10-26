from bmstu_lab.models import Company
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Company
        # Поля, которые мы сериализуем
        fields = ["id", "name_company", "product", "description"]