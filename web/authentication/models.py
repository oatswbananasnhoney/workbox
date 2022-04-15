from django.db import models as m
from django.contrib.auth.models import User as U
from django.db.models.signals import post_save
from django.dispatch import receiver
""" from pm.models import W,P """
class P(m.Model):
    user=m.OneToOneField(U,on_delete=m.CASCADE,related_name='profile')
    n=m.CharField(max_length=333,null=True)
    #favorite_workbox=m.ManyToManyField(W)
    #favorite_project=m.ManyToManyField(P)
    def __str__(self):
        return self.n
    class Meta:
        ordering=['user']
@receiver(post_save, sender=U)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        P.objects.create(user=instance)
    instance.profile.save()