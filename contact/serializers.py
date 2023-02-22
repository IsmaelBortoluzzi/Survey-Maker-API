from django.contrib.auth.models import User
from rest_framework import serializers

from contact.models import Contact, Country, State, City


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class ContactSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField(read_only=True)
    city_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=City.objects.all())
    user_object = UserSerializer(many=False, source='user', read_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)

    class Meta:
        model = Contact
        fields = (
            'user_object', 'city', 'city_id', 'gender',
            'birthday', 'first_name', 'last_name', 'email',
            'password', 'username'
        )


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
