from django.shortcuts import render
from django.utils import timezone
from todo.models import Todo
from django.http import HttpResponseRedirect
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request , 'todo/index.html' , {"todo_items":todo_items})

def add_todo(request):
    Current_date = timezone.now()
    content = request.POST["content"]
    created_obj = Todo.objects.create(added_date = Current_date , text = content )
    length_of_todos = Todo.objects.all().count()
    return HttpResponseRedirect('/')

def delete_todo(request , todo_id):
    Todo.objects.get(id = todo_id).delete()
    return HttpResponseRedirect('/')
