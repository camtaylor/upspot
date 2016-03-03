from django.contrib.auth.models import User, Group
from park.models import Spot
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'email', 'rating')

class SpotSerializer(serializers.ModelSerializer):
  class Meta:
    model = Spot
    fields = ('owner', 'address', 'location', 'available')
