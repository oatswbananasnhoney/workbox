from django.db import models as m
from django.contrib.auth.models import User as U
from tinymce.models import HTMLField as h
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from uuid import uuid4 as u4
from tinymce.models import HTMLField as h
from django.utils.translation import gettext_lazy as _

""" class M(m.Model):
    subject=m.CharField(max_length=100)
    content=h()
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name='Message'
        ordering=['subject'] """
class W(m.Model):
    title=m.CharField(max_length=100)
    description=m.TextField(max_length=999)
    member=m.ManyToManyField('P',related_name='workbox_member')
    uid=m.UUIDField(default=u4)
    owner=m.ForeignKey(U,on_delete=m.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'workbox/{self.uid}/'
    class Meta:
        verbose_name='Workbox'
        verbose_name_plural='Workboxes'
        ordering=['title']
class T(m.Model):
    PRIORITY=(
        ('l','Низкий'),
        ('m','Средний'),
        ('h','Высокий'),
        ('n','Нет Приоритета'),
    )
    title=m.CharField(_("Заголовок"),max_length=100)
    uid=m.UUIDField(default=u4)
    completed=m.BooleanField(_("Завершена?"),default=False)
    creator=m.ForeignKey(U,on_delete=m.CASCADE)
    due_date=m.DateField(_("Конец Дата"),blank=True,null=True)
    due_time=m.TimeField(_("Конец Время"),blank=True,null=True)
    description=h(_("Описание"),blank=True,null=True)
    project=m.ForeignKey('P',on_delete=m.CASCADE,blank=True,null=True,verbose_name='Проект')
    priority=m.CharField(_("Важность"),choices=PRIORITY,max_length=10,blank=True,null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'task/{self.uid}/'
    class Meta:
        verbose_name='Task'
        ordering=['title']
        
class P(m.Model):
    STATUS=(
        ('ont','On track'),
        ('ar','At risk'),
        ('oft','Off track'),
        ('oh','On hold'),
        ('c','Complete'),
    )
    uid=m.UUIDField(default=u4)
    workbox=m.ForeignKey(W,on_delete=m.CASCADE)
    title=m.CharField(max_length=100)
    color=m.CharField(max_length=100,default='#FFA145')
    #icon=m.FileField(blank=True,null=True)
    owner=m.ForeignKey(U,on_delete=m.CASCADE,blank=True,null=True)
    description=h(blank=True,null=True)
    due_date=m.DateField(blank=True,null=True)
    status=m.CharField(max_length=20,choices=STATUS,blank=True,null=True)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'project/{self.uid}/'
    class Meta:
        verbose_name='Project'
        ordering=['title']
@receiver(post_save, sender=U)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        t='Пробный Workbox'
        W.objects.create(owner=instance,title=t)
    instance.profile.save()