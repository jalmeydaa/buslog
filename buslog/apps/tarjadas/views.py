from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404

from .models import Chofer
from .serializers import ChoferSerializer,UserSerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.reverse import reverse
from rest_framework import status,mixins,generics,permissions,renderers


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
	return Response({
		'users': reverse('tarjadas:user-list', request=request, format=format),
		'choferes': reverse('tarjadas:chofer-list', request=request, format=format)
	})


class ChoferHighlight(generics.GenericAPIView):
	queryset = Chofer.objects.all()
	renderer_classes = (renderers.StaticHTMLRenderer,)

	def get(self, request, *args, **kwargs):
		chofer = self.get_object()
		return Response(chofer.highlighted)


class ChoferList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = Chofer.objects.all()
	serializer_class = ChoferSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class ChoferDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
	queryset = Chofer.objects.all()
	serializer_class = ChoferSerializer


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


'''
class ChoferList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
	queryset = Chofer.objects.all()
	serializer_class = ChoferSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
	queryset = Chofer.objects.all()
	serializer_class = ChoferSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
'''

'''
class ChoferList(APIView):
	"""
	Lista todos los choferes, o crea un chofer nuevo.
	"""
	def get(self, request, format=None):
		choferes = Chofer.objects.all()
		serializer = ChoferSerializer(choferes, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ChoferSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''


'''
class ChoferDetail(APIView):
	"""
	Retorna, actualiza o elimina un chofer.
	"""
	def get_object(self, pk):
		try:
			return Chofer.objects.get(pk=pk)
		except Chofer.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		chofer = self.get_object(pk)
		serializer = ChoferSerializer(chofer)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		chofer = self.get_object(pk)
		serializer = ChoferSerializer(chofer, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		chofer = self.get_object(pk)
		chofer.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
'''