from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer

UserModel = get_user_model()


class RegisterSerializer(ModelSerializer):

    # Hash the password in the DB and the response
    def create(self, validated_data):
        user = super(RegisterSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    # Adds password validation
    @staticmethod
    def validate_password(value):
        from rest_framework.exceptions import ValidationError
        try:
            validate_password(value)
        except ValidationError as exc:
            raise ValidationError(str(exc))
        return value

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'email', 'date_of_birth', 'gender', 'password')

