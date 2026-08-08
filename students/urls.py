from django.urls import path
from . import views

urlpatterns = [
    # General Views
    path('', views.home_view, name='home'),
    path('students/', views.student_list_view, name='student_list'),
    path('students/active/', views.active_student_list_view, name='active_student_list'),
    path('students/about/', views.about_view, name='about'),
    path('students/contact/', views.contact_view, name='contact'),
    
    # Student CRUD Views
    path('students/create/', views.student_create_view, name='student_create'),
    path('students/<int:pk>/edit/', views.student_update_view, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete_view, name='student_delete'),
    
    # Student Detail and Name Search
    path('students/<int:student_id>/', views.student_detail_view, name='student_detail'),
    path('students/name/<str:name>/', views.student_name_view, name='student_name'),

    # Course CRUD Views (Task 20 Extension)
    path('courses/', views.course_list_view, name='course_list'),
    path('courses/create/', views.course_create_view, name='course_create'),
    path('courses/<int:pk>/', views.course_detail_view, name='course_detail'),
    path('courses/<int:pk>/edit/', views.course_update_view, name='course_update'),
    path('courses/<int:pk>/delete/', views.course_delete_view, name='course_delete'),
]