from rest_framework import routers
from .views import TodoViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register("todo", TodoViewSet)

app_name = "api"

urlpatterns = [
    path('', include(router.urls))
]