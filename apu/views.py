from django.shortcuts import render, HttpResponse
from . models import Roadmap, Milestone
from . serializers import RoadmapSerializer, MilestoneSerializer, ActionSerializer, RoadmapCatlogSerializer, FileSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser


def home(request):

	return HttpResponse('HOMEBITCH')


class RoadmapView(viewsets.ModelViewSet):
	queryset = Roadmap.objects.all()	
	serializer_class = RoadmapSerializer
	parser_classes = (MultiPartParser, FormParser)
	
	def list(self, request):
		road = Roadmap.objects.all()
		serializer_context = {
			'request': request,
		}
		serialized = RoadmapCatlogSerializer(road, many=True,context=serializer_context)

		return Response(serialized.data)

	def post(self, request, *args, **kwargs):

		file_serializer = FileSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)














# @action(detail=False, methods=['GET'])
# def filter_shippings(self, request, **kwargs):
#     queryset = self.get_queryset().filter(status=2, orderStatus=0)
#     serializer = SearchShippingSerializer(queryset, many=True) #Yes, I am using another serializer, but it is solved,I use diferent if it is necesary
#     return Response(serializer.data)