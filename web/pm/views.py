from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect as HRR
from django.contrib.auth.decorators import login_required as lr
from datetime import date
import calendar
from datetime import datetime as dt

from .functions import time_of_day

from .forms import PF,TF,TEF
from authentication.models import P
from .models import W,T
from .models import P as Pr
n=dt.now()
d=date.today()
wd=calendar.day_name[d.weekday()]
m=n.strftime('%B')
d=n.strftime('%d')

tod=time_of_day(n.hour)
def h(request):
    c={}
    if request.user.is_authenticated:
        p=P.objects.get(user=request.user)
        w=W.objects.filter(owner=request.user)
        nct=len(T.objects.filter(completed=True))
        c['wd'],c['m'],c['d'],c['tod'],c['p'],c['w'],c['nct']=wd,m,d,tod,p,w,nct
    return render(request,'h.html',c)
@lr
def w(request,question_id):
    w=W.objects.filter(owner=request.user)
    cw=get_object_or_404(W,uid=question_id)
    p=Pr.objects.filter(workbox=cw)
    c,c['w'],c['cw'],c['p']={},w,cw,p
    return render(request,'pm/w.html',c)
def project(request,question_id):
    w=W.objects.filter(owner=request.user)
    p=get_object_or_404(Pr,uid=question_id)
    t=T.objects.filter(project=p)
    c,c['w'],c['t'],c['p']={},w,t,p
    return render(request,'pm/p.html',c)
def cp(request):
    id=request.GET.get('id')
    w=get_object_or_404(W,uid=id)
    if request.method=='POST':
        project_form=PF(request.POST)
        if project_form.is_valid():
            project_form.instance.owner=request.user
            project_form.instance.workbox=w
            project_form.save()
            return redirect('/workbox/{}'.format(w.uid))
    else:
        project_form=PF()
    c,c['pf'],c['w']={},PF(),w
    return render(request,'pm/cp.html',c)
def create_task(request):
    id=request.GET.get('id')
    p=get_object_or_404(Pr,uid=id)
    if request.method=='POST':
        project_form=TF(request.POST)
        if project_form.is_valid():
            project_form.instance.creator=request.user
            project_form.instance.project=p
            project_form.save()
            return redirect('/project/{}'.format(p.uid))
    else:
        project_form=TF()
    c,c['task_form'],c['p']={},TF(),p
    return render(request,'pm/ct.html',c)
def my_tasks(request):
    c,c['t'],c['w']={},T.objects.filter(creator=request.user),W.objects.filter(owner=request.user)
    return render(request,'pm/mt.html',c)
def create_my_task(request):
    if request.method=='POST':
        task_form=TF(request.POST)
        if task_form.is_valid():
            task_form.instance.creator=request.user
            task_form.save()
            return redirect('/my-tasks/')
    else:
        task_form=TF()
    c,c['task_form']={},TF
    return render(request,'pm/cmt.html',c)
def task(request, question_id):
    task = get_object_or_404(T, uid=question_id)
    if request.method == "POST":
        form = TEF(request.POST,
                        instance=task)
        if form.is_valid():
            form.save()
            return redirect('post_create')
    else:
        form = TEF(instance=task)

    return render(request,'pm/t.html',{'task_form': form,'task': task})