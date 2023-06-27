from rest_framework import serializers
from .models import Sentimenttb
from setfit import SetFitModel

class SentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentimenttb
        fields = '__al__'