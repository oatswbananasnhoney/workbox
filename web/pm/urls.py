from django.urls import path
from .views import h,w,cp,my_tasks,create_my_task,task,project,create_task
urlpatterns=[
    path('',h,name='h'),
    path('workbox/<uuid:question_id>/',w),
    path('project/<uuid:question_id>/',project),
    path('task/<uuid:question_id>/',task),
    path('create-project/',cp,name='cp'),
    path('my-tasks/',my_tasks,name='my_tasks'),
    path('create-my-task/',create_my_task,name='create_my_task'),
    path('create-task/',create_task,name='create_task'),
]