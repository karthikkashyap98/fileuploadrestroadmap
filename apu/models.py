from django.db import models


class Roadmap(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()

	@property
	def milestones(self):
		milestones = Milestone.objects.filter(roadmaplink=self)
		return list(milestones)


	@property	
	def file(self):
		file = File.objects.filter(roadmap=self)
		return file




	def __str__(self):
		return f"{self.title}"


class Milestone(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	roadmaplink = models.ForeignKey(Roadmap, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.title}"

	@property
	def actions(self):
		actions = Action.objects.filter(milestonelink=self).values('id', 'title', 'body')
		return list(actions)


class Action(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	milestonelink = models.ForeignKey(Milestone, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.title}"

class File(models.Model):
	 file = models.FileField(blank=False, null=False)
	 timestamp = models.DateTimeField(auto_now_add=True)
	 roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE)