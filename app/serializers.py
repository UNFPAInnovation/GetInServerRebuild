import jwt
from djoser.serializers import TokenSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.utils import jwt_payload_handler

from GetInBackendRebuild.settings import SECRET_KEY
from app.models import User, District, County, SubCounty, Parish, Village, Girl, HealthFacility, FollowUp, Delivery, \
    MappingEncounter, AppointmentEncounter, Appointment, SmsModel, Observation, FamilyPlanning


def create_token(user=None):
    payload = jwt_payload_handler(user)
    token = jwt.encode(payload, SECRET_KEY)
    return token.decode('unicode_escape')


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email', 'phone', 'password', 'gender', 'village', 'number_plate',
            'role', 'midwife')

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
            'id', 'first_name', 'last_name', 'username', 'email', 'gender', 'village', 'number_plate', 'role', 'phone')


class DistrictGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class CountyGetSerializer(serializers.ModelSerializer):
    district = DistrictGetSerializer(many=False, read_only=True)

    class Meta:
        model = County
        fields = '__all__'


class SubCountyGetSerializer(serializers.ModelSerializer):
    county = CountyGetSerializer(many=False, read_only=True)

    class Meta:
        model = SubCounty
        fields = '__all__'


class ParishGetSerializer(serializers.ModelSerializer):
    sub_county = SubCountyGetSerializer(many=False, read_only=True)

    class Meta:
        model = Parish
        fields = '__all__'


class VillageGetSerializer(serializers.ModelSerializer):
    parish = ParishGetSerializer(many=False, read_only=True)
    parish_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Village
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    village = VillageGetSerializer(many=False, read_only=True)
    midwife = UserGetSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'username', 'email', 'phone', 'password', 'gender', 'village',
            'number_plate',
            'role', 'midwife', 'user_permissions', 'created_at')
        # extra_kwargs = {"password": {"write_only": True}}

    def validate_phone(self, value):
        # user can only register one phone number
        user = User.objects.filter(phone=value)
        if user.exists():
            raise ValidationError("This user has already registered with the phone number")
        return value

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


class HealthFacilityGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthFacility
        fields = (
            'id', 'sub_county', 'name')


class GirlSerializer(serializers.ModelSerializer):
    village = VillageGetSerializer(many=False, read_only=True)
    village_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Girl
        # list all the fields since the age property is not picked up by __all__
        fields = (
            'id', 'first_name', 'last_name', 'village', 'village_id', 'phone_number', 'trimester',
            'next_of_kin_phone_number', 'education_level', 'marital_status',
            'last_menstruation_date', 'dob', 'user', 'odk_instance_id', 'age', 'completed_all_visits',
            'pending_visits', 'missed_visits', 'created_at')


class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = '__all__'


class FamilyPlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyPlanning
        fields = '__all__'


class FollowUpGetSerializer(serializers.ModelSerializer):
    girl = GirlSerializer(read_only=True)
    observation = ObservationSerializer(read_only=True)

    class Meta:
        model = FollowUp
        fields = '__all__'


class FollowUpPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUp
        fields = '__all__'


class DeliveryGetSerializer(serializers.ModelSerializer):
    girl = GirlSerializer(read_only=True)
    health_facility = HealthFacilityGetSerializer()
    family_planning = FamilyPlanningSerializer(read_only=True, many=True)

    class Meta:
        model = Delivery
        fields = '__all__'


class DeliveryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class MappingEncounterSerializer(serializers.ModelSerializer):
    girl = GirlSerializer(read_only=True)
    family_planning = FamilyPlanningSerializer(read_only=True, many=True)
    observation = ObservationSerializer(read_only=True)
    user = UserGetSerializer(read_only=True)

    class Meta:
        model = MappingEncounter
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    girl = GirlSerializer(read_only=True)
    user = UserGetSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentEncounterSerializer(serializers.ModelSerializer):
    observation = ObservationSerializer(read_only=True)
    appointment = AppointmentSerializer(read_only=True)

    class Meta:
        model = AppointmentEncounter
        fields = '__all__'


class CustomTokenSerializer(TokenSerializer):
    """
    Override the djoser(https://djoser.readthedocs.io/en/latest/) token serializer
    Allows us to return user details along side the djoser token
    """
    auth_token = serializers.CharField(source='key')
    user = UserSerializer()

    class Meta:
        model = Token
        fields = (
            'auth_token', 'user'
        )


class SmsModelSerializer(serializers.ModelSerializer):
    recipient = UserGetSerializer()

    class Meta:
        model = SmsModel
        fields = (
            'id', 'recipient', 'sender_id', 'message', 'status', 'created_at')
