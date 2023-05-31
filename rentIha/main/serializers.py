from rest_framework import serializers
from .models import Iha, Rent


class IhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iha
        fields = ['id', 'brand', 'model' , 'weight' , 'category']


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'
