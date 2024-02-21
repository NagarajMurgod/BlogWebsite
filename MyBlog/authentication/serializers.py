
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.core.validators import EmailValidator
from django.contrib.auth.password_validation import validate_password


User = get_user_model()

class CreateUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'confirm_password'
        ]

        extra_kwargs = {
            "email" : {
                'validators' : [EmailValidator]
            }
        }

    
    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('confirm_password')

        if password != password2:
            raise serializers.ValidationError("password doesn't match")
        return attrs


    def validate_password(self,value):
        validate_password(value)
        return value

    def validate_email(self,value):
        user = User.objects.filter(email=value.lower())
       
        if user.exists():
            raise serializers.ValidationError('Email address is already exist')

        return  value.lower()

    def create(self, validated_data):
        user = User.objects.create(email = validated_data['email'],password=validated_data['password'])
        user.save()
        return user
    


class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)


    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(self.context.get('request'), email=email, password=password)
            if user is None:
                raise serializers.ValidationError('Wrong username and password')
            attrs['user'] = user
        
        else:
            raise serializers.ValidationError('Both email and password are required')
        
        
        return attrs

    
    def validate_email(self,value):
        return value.lower()

        
        
