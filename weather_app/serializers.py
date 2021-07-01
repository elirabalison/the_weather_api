from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    """Serialize the weather temperature result"""

    maximum = serializers.FloatField()
    minimum = serializers.FloatField()
    average = serializers.FloatField()
    median = serializers.FloatField()