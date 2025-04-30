# # from django.shortcuts import render
# # from django.http import HttpResponse

# # def home(request):
# #     return render(request,'home.html',{'name':"Vansh"})
# # def add(request):
# #     val1 = int(request.GET['num1'])
# #     val2 = int(request.GET['num2'])
# #     operation = request.GET["operation"]

# #     if operation=="+":
# #         result = val1 +val2
        
# #     elif operation=="-":
# #         result = val1 - val2
        
# #     elif operation =="*":
# #         result = val1 * val2
        
# #     elif operation == "/":
# #         result = val1/val2
        
# #     else:
# #         result = "invalid"
        
# #     return render(request,'result.html',{'result': result})
# # Create your views here.
# from django.shortcuts import render

# def home(request):
#     return render(request, 'home.html')

# def add(request):
#     val1 = int(request.GET['num1'])
#     val2 = int(request.GET['num2'])
#     operation = request.GET['operation']

#     if operation == '+':
#         result = val1 + val2
#     elif operation == '-':
#         result = val1 - val2
#     elif operation == '*':
#         result = val1 * val2
#     elif operation == '/':
#         result = val1 / val2
#     else:
#         result = "Invalid operation"

#     return render(request, 'result.html', {'result': result})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.utils import timezone

def task_list(request):
    tasks = Task.objects.all().order_by('due_date')
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST.get('due_date') or None
        if due_date:
            due_date = timezone.datetime.fromisoformat(due_date)
        Task.objects.create(title=title, description=description, due_date=due_date)
        return redirect('task_list')
    return render(request, 'add_task.html')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
def task_list(request):
    tasks = Task.objects.all().order_by('due_date')
    return render(request, 'task_list.html', {
        'tasks': tasks,
        'now': timezone.now()
    })