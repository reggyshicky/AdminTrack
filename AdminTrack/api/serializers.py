from rest_framework import serializers
from Books.models import Book
from Teacher.models import Teacher
from Students.models import Student
from Employees.models import Employee
from Attendance.models import Attendance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


#the serializer classes are used to transform complex data types in this case
# a django model into native python data types(serialization) and vice versa (deserialization)