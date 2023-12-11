from rest_framework import serializers
from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    author = models.CharField(max_length=100)
    duration = models.FloatField()
    discount = models.IntegerField(default=0)
    
    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"