from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.projecthomepage, name='projecthomepage'),
    path('printpagecall/',views.printpagecall, name='printpagecall'),
    path('printpagelogic/',views.printpagelogic, name='printpagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall, name='exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic, name='exceptionpagelogic'),
    path('randompagecall/', views.randompagecall, name='randompagecall'),
    path('randomlogic/', views.randomlogic, name='randomlogic'),
    path('calculatorpagecall/',views.calculatorpagecall, name='calculatorpagecall'),
    path('calculatorlogic/',views.calculatorlogic, name='calculatorlogic'),
    path('datetimepagecall/', views.datetimepagecall, name='datetimepagecall'),
    path('datetimepagelogic/', views.datetimepagelogic, name='datetimepagelogic'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task,name='delete_task'),
    path('userregisterpagecall/',views.userregisterpagecall,name='userregisterpagecall'),
    path('userregisterlogic/',views.userregisterlogic,name='userregisterlogic'),
    path('UserLoginPageCall/',views.UserLoginPageCall,name='UserLoginPageCall'),
    path('UserLoginLogic/',views.UserLoginLogic,name='UserLoginLogic'),
    path('logout/',views.logout,name='logout'),
    path('student_list/',views.student_list,name='student_list'),
    path('add_student/',views.add_student,name='add_student'),
    path('contact_list/', views.contact_list, name='contact_list'),
    path('add/', views.add_contact, name='add_contact'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('send/<int:pk>/', views.send_contact_email, name='send_contact_email'),

]