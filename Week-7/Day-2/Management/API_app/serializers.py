from rest_framework import serializers
from .models import Department, Task, Project, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):

    department = serializers.HyperlinkedIdentityField(view_name='department-link')

    class Meta:
        model = Employee
        fields = '__all__'
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):

    project = serializers.HyperlinkedIdentityField(view_name='project-link')

    class Meta:
        model = Task
        fields = '__all__'

