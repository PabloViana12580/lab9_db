from rest_framework import serializers
from . import models

class chismes_serializer(serializers.ModelSerializer):
	class Meta:
		model = models.Chismes
		fields = '__all__'