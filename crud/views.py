from django.shortcuts import render,redirect
from .forms import employeeform
from .models import employee



def insert(request):
    if request.method=='POST':
        form=employeeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/select')
    else:
        form=employeeform()
    return render(request,'home.html',{'form':form})

def select(request):
    employees=employee.objects.all()
    return render(request,"select.html",{'employees':employees})

def edit(request, Id):
    employees = employee.objects.get(Id=Id)
    form=employeeform(instance=employees)
    if request.method=="POST":
        form = employeeform(request.POST, instance=employees)
        if form.is_valid():
            form.save()
            return redirect("/select")
    return render(request, 'edit.html', {'form': form})

def delete(request, Id):
    employees=employee.objects.get(Id=Id)
    employees.delete()
    return redirect('/select')

