from django.contrib import admin as a
from .models import W,P,T

a.site.register(W)
a.site.register(P)
a.site.register(T)