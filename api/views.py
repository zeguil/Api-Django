from rest_framework import viewsets
from api.models import Student
from api.serializer import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



