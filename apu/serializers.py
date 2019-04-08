from rest_framework import serializers
from .models import Roadmap, Milestone, Action, File



class ActionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Action 
		fields = ('id','title','body')



class MilestoneSerializer(serializers.ModelSerializer):
	actions = ActionSerializer(many=True)
	class Meta:
		model = Milestone
		fields = ('id','title','body', 'actions')
		depth = 1

class FileSerializer(serializers.ModelSerializer):
	class Meta:
		model = File
		fields = ('file', 'timestamp')

class RoadmapSerializer(serializers.ModelSerializer):
	milestones = MilestoneSerializer(many=True)
	file = FileSerializer(many=True)
	class Meta:
		model = Roadmap
		fields = ('id','title','body','file','milestones')
		depth = 1


class RoadmapCatlogSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Roadmap
		fields = ('url','id','title','body')


