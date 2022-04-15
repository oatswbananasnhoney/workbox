from django.urls import path
from .views import l,r
from django.contrib.auth.views import LogoutView as LV
from django.conf import settings as s
urlpatterns=[
    path('login/',l,name='login'),
    path('logout/',LV.as_view(),{'next_page': s.LOGOUT_REDIRECT_URL},name='logout',),
    path('register/',r,name='register'),
]