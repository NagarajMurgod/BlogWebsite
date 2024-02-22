
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.core.validators import EmailValidator,validate_email
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
        user = User.objects.create_user( username=validated_data['email'], email = validated_data['email'],password=validated_data['password'])
        user.save()
        return user
    


class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)



    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        print(email, password)
        if email and password:
            user = authenticate(request=self.context.get('request'), email=email.lower(), password=password)
            print(user)
            if user is None:
                raise serializers.ValidationError('Wrong username and password')
            attrs['user'] = user
        
        else:
            raise serializers.ValidationError('Both email and password are required')
        
        
        return attrs

    
    def validate_email(self,value):
        validate_email(value)
        return value.lower()

        
        
