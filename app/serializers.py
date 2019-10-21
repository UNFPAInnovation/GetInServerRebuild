import jwt
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import EmailField, CharField
from rest_framework.settings import api_settings
from rest_framework_jwt.utils import jwt_payload_handler

from GetInBackendRebuild.settings import SECRET_KEY
from app.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'phone', 'createdAt',)
        # extra_kwargs = {"password": {"write_only": True}}

    def validate_phone(self, value):
        # user can only register one phone number
        user = User.objects.filter(phone=value)
        if user.exists():
            raise ValidationError("This user has already registered with the phone number")
        return value

    def validate(self, data):
        return data

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            # username is a combination of first and last name
            username=validated_data['first_name'] + validated_data['last_name'],
            email=validated_data['email'],
            phone=validated_data['phone'],
        )
        user.set_password(validated_data['phone'])
        user.save()
        return user


def create_token(user=None):
    payload = jwt_payload_handler(user)
    token = jwt.encode(payload, SECRET_KEY)
    return token.decode('unicode_escape')


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email', 'phone', 'password', 'gender')

    def create(self, validated_data):
        """
        Sets user password.
        NOTE: Without this, User will never sign_in and password will not be encrypted
        """
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'gender')


class DistrictGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = (
            'id', 'name')


class CountyGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = (
            'id', 'district', 'name')


class SubCountyGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCounty
        fields = (
            'id', 'county', 'name')


class ParishGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parish
        fields = (
            'id', 'sub_county', 'name')


class VillageGetSerializer(serializers.ModelSerializer):
    parish = ParishGetSerializer(many=False, read_only=True)
    parish_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Village
        fields = '__all__'


class HealthFacilityGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthFacility
        fields = (
            'id', 'parish', 'name')


class GirlSerializer(serializers.ModelSerializer):
    village = VillageGetSerializer(many=False, read_only=True)
    village_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Girl
        fields = '__all__'


class FollowUpGetSerializer(serializers.ModelSerializer):
    girl = GirlSerializer()
    user = UserGetSerializer()

    class Meta:
        model = FollowUp
        fields = '__all__'


class FollowUpPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUp
        fields = '__all__'


class DeliveryGetSerializer(serializers.ModelSerializer):
    girl = GirlSerializer()
    user = UserGetSerializer()

    class Meta:
        model = Delivery
        fields = '__all__'


class DeliveryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'
