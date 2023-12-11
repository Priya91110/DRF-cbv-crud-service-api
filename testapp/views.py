from django.shortcuts import render
from .models import Course, CourseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Create your views here.

class CourseListView(APIView):
    #for  get and post 
    
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    
        
class CourseDetailView(APIView):
    #to fetch id
    def get_course(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except course.DoesNotExits:
            raise Http404
        
    #  for get, put, delete
    def get(self, request, pk):
        course = self.get_course(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        course = self.get_course(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        course = self.get_course(pk)
        serailzer = CourseSerializer(course, data=request.data)
        if serailzer.is_valid():
            serailzer.save()
            return Response(serailzer.data)
        else:
            return Response(serailzer.errors)
        
        