from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookSerializer, TeacherSerializer, StudentSerializer
from .serializers import EmployeeSerializer, AttendanceSerializer
from Books.models import Book
from Teacher.models import Teacher
from Students.models import Student
from Employees.models import Employee
from Attendance.models import Attendance

## STUDENTS API
@api_view(["GET"])
def student_list(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
@api_view(["POST"])
def post_student(request):
    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

## BOOKS API
@api_view(["GET"])
def book_list(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
@api_view(["POST"])
def add_book(request):
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# TEACHERS APIS
@api_view(["GET"])
def teacher_list(request):
    if request.method == "GET":
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
@api_view(["POST"])
def add_teacher(request):
    if request.method == "POST":
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def teacher_detail(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
# EMPLOYEES APIS
@api_view(['GET'])
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def post_employee(request):
    if request.method == "POST":
      serializer = EmployeeSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def employee_details(request, id):
    try:
        employee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#ATTENDANCE APIS
@api_view(['GET'])
def attendance_list(request):
    if request.method == "GET":
        attendance = Attendance.objects.all()
        serializer = AttendanceSerializer(attendance, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def post_attendance(request):
    serializer = AttendanceSerializer(data=request.data)
    if request.method == "POST":
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error, status-status.HTTP_400_BAD_REQUEST)
        
@api_view(['PUT', 'GET', 'DELETE'])
def attendance_details(request, id):
    try:
        attendance = Attendance.objects.get(pk=id)
    except Attendance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == "GET":
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data)
          
    elif request.method == "PUT":
        serializer = AttendanceSerializer(attendance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    
    elif request.method == "DELETE":
        attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


    

    
        
    