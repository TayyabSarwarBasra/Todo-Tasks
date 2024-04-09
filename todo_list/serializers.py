from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Todo, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'deadline', 'priority', 'status', 'category']
        extra_kwargs = {
            'title': {'required': True},
            'deadline': {'required': True},
            'category': {'required': False},
        }


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
