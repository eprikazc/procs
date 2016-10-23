
from rest_framework import serializers
from .models import Proc, Bread, Hat, Money, Doc, Person


class HatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hat
        fields = '__all__'


class BreadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bread
        fields = '__all__'


class ProcSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proc
        fields = '__all__'


class MoneySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Money
        fields = '__all__'


class DocSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doc
        fields = '__all__'


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
