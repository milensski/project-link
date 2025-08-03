from rest_framework import serializers


class LogoutSerializer(serializers.Serializer):
    """
    Serializer for the LogoutView.
    Does not require any input, but provides a clear response structure.
    """
    detail = serializers.CharField(read_only=True, default="Successfully logged out.")
