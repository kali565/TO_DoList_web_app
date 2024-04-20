from django.shortcuts import render,HttpResponse,redirect
from home.models import Task
from django.core.exceptions import ObjectDoesNotExist 
from django import forms
# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == "POST":
        #handel the form
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        ins=Task(tasktitle=title,taskdesc=desc)
        ins.save()
        context ={'success': True}
    return render(request,'index.html',context)

def tasks(request):
    allTasks=Task.objects.all()
  #  for item in allTasks:
   #     print(item.taskdesc)
    context={'tasks':allTasks}
    return render(request,'tasks.html',context)

def delete_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
    except Task.DoesNotExist:  # Catch DoesNotExist exception
        # Handle the case where the task does not exist
        pass  # You can log the error, display a message, or take other actions
    return redirect('tasks')

def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update_task.html', {'form': form})

# Modify tasks view to handle delete and update actions
def tasks(request):
    if request.method == 'POST':
        # Handle form submissions for update
        task_id = request.POST.get('task_id')
        if 'delete' in request.POST:
            return delete_task(request, task_id)
        elif 'update' in request.POST:
            return update_task(request, task_id)
    else:
        allTasks = Task.objects.all()
        return render(request, 'tasks.html', {'tasks': allTasks})
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['tasktitle', 'taskdesc','completed']
    