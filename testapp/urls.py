
from django.contrib import admin
from django.urls import path, include
from testapp import views
urlpatterns = [
    path('courses', views.CourseListView.as_view()),
    path('courses/<int:pk>', views.CourseDetailView.as_view())
 
]