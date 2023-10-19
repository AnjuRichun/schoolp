from detailapp import views
from django.urls import path
app_name='detailapp'
urlpatterns=[
    path('detail/<id>',views.detail,name='detail'),
    path('new',views.new,name='new'),
    path('add',views.StudentCreateView.as_view(),name='student_add'),
    path('ajax-load-course',views.load_course,name='ajax_load_course'),
    path('addnew',views.addnew,name='addnew'),
]