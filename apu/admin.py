    
from django.contrib import admin
from .models import Roadmap, Milestone, Action, File


admin.site.register(Roadmap)
admin.site.register(Milestone)
admin.site.register(Action)
admin.site.register(File)
