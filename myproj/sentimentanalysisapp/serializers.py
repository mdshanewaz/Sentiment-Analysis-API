from rest_framework import serializers
from .models import Sentimenttb

class SentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentimenttb
        fields = '__al__'