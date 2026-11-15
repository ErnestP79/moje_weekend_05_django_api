from django.urls import include, path
from .views import health_check, tasks_list_text, home, TaskListAPIView, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path("health2/", include("tasks.health_urls")),
    path("", home, name="home"),
    path("health/", health_check, name="health"),
    path("tasks/", tasks_list_text, name="tasks-list-text"),
    path("api/", include(router.urls)),
]