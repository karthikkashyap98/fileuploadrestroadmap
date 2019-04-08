from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls.static import static
from rest_api import settings


router = routers.DefaultRouter()
router.register('roadmap', views.RoadmapView)


urlpatterns = [
 	
 	path('', include(router.urls))
	# path('roadmap/', views.RoadmapView.as_views())
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

