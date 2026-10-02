from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.db.models import QuerySet
from rest_framework import serializers

from .models import Category, Comment, Post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields="__all__"
        
class PostSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty")
        return value

    def validate_content(self, value):
        if len(value.strip())<10:
            raise serializers.ValidationError(
                "Content must contain atleast 10 characters."
            )
        return value

    category_id=serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )
    category=CategorySerializer(read_only=True)
    comments=CommentSerializer(many=True, read_only=True)
    class Meta:
        model=Post
        fields="__all__"


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        return user

    def validate_password(self, value):
        user = User(
            username=self.initial_data.get("username", ""), # type: ignore
            email=self.initial_data.get("email", ""), # type: ignore
        )
        validate_password(value, user=user)
        return value

    def validate_email(self, value):
        mail=User.objects.filter(email__iexact=value).exists()

        if mail:
            raise serializers.ValidationError("This email is already exists.")
        return value

    class Meta:
            model= User
            fields=['username', 'email', 'password']