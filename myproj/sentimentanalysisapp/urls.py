from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeAPIView.as_view(), name='home'),
    path('analyze/', SentimentAPIView.as_view(), name='analyze'),
    
]