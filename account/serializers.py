from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):

    password_confirm = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_confirm']

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User with this email already exists')
        return email

    def validate(self, attrs):
        password1 = attrs['password']
        password2 = attrs.pop('password_confirm')

        if password1 != password2:
            raise serializers.ValidationError('Passwords do not match')
        
        return attrs
    
    def create(self, validated_data):
        print('CREATING USER', validated_data)
        return User.objects.create_user(**validated_data)