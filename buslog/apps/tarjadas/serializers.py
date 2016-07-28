from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class ChoferSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	highlight = serializers.HyperlinkedIdentityField(view_name='tarjadas:chofer-highlight', format='html')

	class Meta:
		model = Chofer
		fields = ('pk','highlight','owner','nombre','code','linenos','language','style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	choferes = serializers.HyperlinkedRelatedField(many=True, view_name='tarjadas:chofer-detail', read_only=True)

	class Meta:
		model = User
		fields = ('pk', 'username', 'choferes')