from rest_framework import serializers

from contact.models import Contact, Country, State, City


class ContactSerializer(serializers.ModelSerializer):
    city_name = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Contact
        fields = ('user', 'city', 'gender', 'birthday')


class CountrySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Country
        fields = ('id', 'name', 'population')


class StateSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = State
        fields = ('id', 'name', 'population', 'country', 'acronym')


class CitySerializer(serializers.ModelSerializer):
    state = serializers.StringRelatedField()
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'population', 'state')
