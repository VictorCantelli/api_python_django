from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Course, Evaluation
from .serializers import CourseSerializer, EvaluationSerializer

class CourseAPIView(APIView):
    """
    Course API
    """
    def get(self, request):
        permission_classes = [IsAuthenticated]
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data)

class EvaluationAPIView(APIView):
    """
    Evaluation API
    """

    def get(self, request):
        permission_classes = [IsAuthenticated]
        evaluations = Evaluation.objects.all()
        serializer = EvaluationSerializer(evaluations, many=True)

        return Response(serializer.data)