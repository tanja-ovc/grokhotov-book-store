"""
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/drf_yasg_integration.html
"""

from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


class TokenObtainPairResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        operation_summary='Получение access и refresh токенов',
        responses={
            status.HTTP_200_OK: TokenObtainPairResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class DecoratedTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        operation_summary='Получение нового access токена по refresh '
                          'токену',
        responses={
            status.HTTP_200_OK: TokenRefreshResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
