from django.urls import path
from .views import CoursesAPIView, EvaluationsAPIView, CourseAPIView, EvaluateAPIView

urlpatterns = [ 
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>', CourseAPIView.as_view(), name='courses'),
    path('courses/<int:course_pk>/evaluations', EvaluationsAPIView.as_view(), name='course_evaluations'),
    path('courses/<int:course_pk>/evaluation/<int:evaluation_pk>', EvaluateAPIView.as_view(), name='course_evaluation'),


    path('evaluations/', EvaluationsAPIView.as_view(), name='evaluations'),
    path('evaluation/<int:evaluation_pk>', EvaluateAPIView.as_view(), name='evaluation'),
    #path('api-token-auth/', AuthTokenAPIView.as_view())
]