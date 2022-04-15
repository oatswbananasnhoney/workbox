from django.contrib.auth.forms import UserCreationForm as UCF
from django.contrib.auth.models import User as U
from django import forms as f
class RF(UCF):
    name=f.CharField(required=True,max_length=333)
    class Meta:
        model = U
        fields = ('username','name','email', 'password1', 'password2',)
