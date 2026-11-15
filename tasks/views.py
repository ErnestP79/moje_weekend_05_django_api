from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer, UserSerializer

tasks_data_example = [
    {
        "id": 1,
        "title": "Create Django project",
        "status": "todo",
        "priority": "high",
    },
    {
        "id": 2,
        "title": "Add health endpoint",
        "status": "in_progress",
        "priority": "medium",
    },
    {
        "id": 3,
        "title": "Prepare API",
        "status": "todo",
        "priority": "high",
    },
]


def health_check(request):
    return HttpResponse("OK")


def health2(request):
    return HttpResponse("Health 2 OK")


def tasks_list_text(request):
    tasks = [
        "1. Przygotowac projekt Django",
        "2. Utworzyc endpoint health",
        "3. Zbudowac liste zadan",
    ]

    return HttpResponse("\n".join(tasks))


def home(request):
    context = {
        "page_title": "Task Manager",
        "tasks_count": len(tasks_data_example),
        "tasks": tasks_data_example,
    }

    return render(request, "home.html", context)

TASKS = [
    {
        "id": 1,
        "title": "Create Django project",
        "description": "Initial setup",
        "status": "todo",
        "priority": "high",
    },
]
USERS = [
    {
        "id": 1,
        "name": "Jan Kowalski",
        "email": "jan@example.com",
    },
    {
        "id": 2,
        "name": "Anna Nowak",
        "email": "anna@example.com",
    },
]


class TaskListAPIView(APIView):

    def get(self, request):
        return Response(
            TASKS,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            new_id = max(
                (task["id"] for task in TASKS),
                default=0
            ) + 1

            new_task = {
                "id": new_id,
                **serializer.validated_data,
            }

            TASKS.append(new_task)

            return Response(
                new_task,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class UserListAPIView(APIView):

    def get(self, request):
        serializer = UserSerializer(USERS, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        return Response(
            request.data,
            status=status.HTTP_201_CREATED
        )    
from rest_framework import viewsets


class TaskViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response(
            TASKS,
            status=status.HTTP_200_OK
        )

    def create(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            new_id = max(
                (task["id"] for task in TASKS),
                default=0
            ) + 1

            new_task = {
                "id": new_id,
                **serializer.validated_data,
            }

            TASKS.append(new_task)

            return Response(
                new_task,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def retrieve(self, request, pk=None):
        for task in TASKS:
            if task["id"] == int(pk):
                return Response(
                    task,
                    status=status.HTTP_200_OK
                )

        return Response(
            {"error": "Task not found"},
            status=status.HTTP_404_NOT_FOUND
        )
