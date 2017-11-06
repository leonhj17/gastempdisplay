# _*_ encoding:utf-8 _*_
from .models import ExpansionKks, MeasureValue
from rest_framework import serializers


class KksSerializer(serializers.ModelSerializer):
    # measurevalue = serializers.StringRelatedField(many=True)

    class Meta:
        model = ExpansionKks
        fields = ('id', 'kks', 'location', 'ab', 'vector')


class MeasureValueSerializer(serializers.ModelSerializer):
    kks = serializers.CharField(source='kks.kks', read_only=True)
    location = serializers.CharField(source='kks.location', read_only=True)
    ab = serializers.CharField(source='kks.ab', read_only=True)
    vector = serializers.CharField(source='kks.vector', read_only=True)
    # kks = serializers.SlugRelatedField(slug_field='location')

    class Meta:
        model = MeasureValue
        fields = ('kks', 'location', 'ab', 'vector', 'value', 'case_time')

