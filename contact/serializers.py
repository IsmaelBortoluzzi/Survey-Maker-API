from rest_framework import serializers

from contact.models import Contact, Country, State, City


class ContactSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()

    class Meta:
        model = Contact
        fields = ('user', 'city', 'is_author', 'gender', 'birthday')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'population')


class StateSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()

    class Meta:
        model = State
        fields = ('name', 'population', 'country', 'acronym')


class CitySerializer(serializers.ModelSerializer):
    state = serializers.StringRelatedField()

    class Meta:
        model = City
        fields = ('name', 'population', 'state')
