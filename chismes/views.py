from rest_framework import viewsets
from rest_framework import mixins
from . import models, serializers
# Create your views here.
class chismes_view_set(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
	queryset = models.Chismes.objects.all()
	serializer_class = serializers.chismes_serializer
	
