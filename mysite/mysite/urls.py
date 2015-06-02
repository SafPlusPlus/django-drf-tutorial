from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from polls import api_views

router = routers.DefaultRouter()
router.register(r'questions', api_views.QuestionViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
]
