from django.shortcuts import render,redirect
from.models import Employee
from django.http import HttpResponse


def showIndex(request):
    qs=Employee.objects.all()
    return render(request,"index.html",{"data":qs})


def saveData(request):
 if request.method=="POST":
    idno=request.POST.get("t1")
    name=request.POST.get("t2")
    salary=request.POST.get("t3")
    doj=request.POST.get("t4")
    designation=request.POST.get("t5")
    Employee(idno=idno,name=name,salary=salary,doj=doj,designation=designation).save()
    qs=Employee.objects.all()
    return render(request,"index.html",{"data":qs})
 else:
     return HttpResponse('invalid request')


def showUpdate(request):
    id=request.POST.get("t1")
    result=Employee.objects.get(idno=id)
    return render(request,"update.html",{"data":result})


def deleteemp(request):
    id=request.POST.get("t1")
    Employee.objects.filter(idno=id).delete()
    return redirect('/index/')


def showdelete(request):
    id=request.GET.get("idno")
    re=Employee.objects.get(idno=id)
    return render(request,"confiremation_delete.html",{"data":re})