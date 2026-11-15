
from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(max_length=200)

    description = serializers.CharField(
        required=False,
        allow_blank=True
    )

    status = serializers.ChoiceField(
        choices=[
            ("todo", "Do zrobienia"),
            ("in_progress", "W trakcie"),
            ("done", "Zrobione"),
        ]
    )

    priority = serializers.ChoiceField(
        choices=[
            ("low", "Niski"),
            ("medium", "Średni"),
            ("high", "Wysoki"),
        ]
    )


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()