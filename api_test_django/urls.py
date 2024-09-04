from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (CoursesAPIView,
                    EvaluationsAPIView,
                    CourseAPIView, 
                    EvaluateAPIView,
                    CourseViewSet,
                    EvaluateViewSet,
                    )


router = SimpleRouter()
router.register('courses', CourseViewSet)
router.register('evaluations', EvaluateViewSet)

urlpatterns = [ 
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>', CourseAPIView.as_view(), name='courses'),
    path('courses/<int:course_pk>/evaluations', EvaluationsAPIView.as_view(), name='course_evaluations'),
    path('courses/<int:course_pk>/evaluation/<int:evaluation_pk>', EvaluateAPIView.as_view(), name='course_evaluation'),


    path('evaluations/', EvaluationsAPIView.as_view(), name='evaluations'),
    path('evaluation/<int:evaluation_pk>', EvaluateAPIView.as_view(), name='evaluation'),
    #path('api-token-auth/', AuthTokenAPIView.as_view())
]