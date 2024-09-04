from rest_framework import serializers

from .models import Course, Evaluation


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Evaluation
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comments',
            'evaluation',
            'creation_date',
            'update_date',
            'isActive'
        )


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'creation_date',
            'isActive'
        )
