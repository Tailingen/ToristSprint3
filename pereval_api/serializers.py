from .models import *
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'


class CoordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coords
        fields = '__all__'


class ImageSerializer(serializers.Serializer):

    class Meta:
        model = Pereval_images
        fields = '__all__'


class PerevalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pereval_added
        fields = ('id', 'users', 'beautyTitle', 'title', 'other_titles', 'connect', 'add_time', 'coord_id',
                  'winter_level', 'spring_level', 'summer_level', 'autumn_level', 'status')

    def create(self, validated_data, **kwargs):
        pereval = Pereval_added.objects.create(**validated_data)
        return pereval


class PerevalSubmitDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval_added
        fields = '__all__'


class PerevalSubmitDataUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval_added
        exclude = ('date_added', 'add_time')
