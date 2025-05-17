from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.Signup,name='signup'),
    path('',views.base),
    path('student_list/',views.student_list,name='student_list'),
    path('edit_student/',views.edit_student,name='edit_student'),
]
