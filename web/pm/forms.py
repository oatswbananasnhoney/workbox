from django.forms import ModelForm as MF
from .models import P,T
class PF(MF):
    class Meta:
        model=P
        fields=('color','title','description',)
class TF(MF):
    class Meta:
        model=T
        fields=('title',)
class TEF(MF):
    class Meta:
        model=T
        fields=('title','completed','project','priority','due_date','due_time','description',)