from todo.forms import CreateTodoForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import ToDo


# Create your views here.

def index(request):
  if(request.method == 'POST'):
    create_todo_form = CreateTodoForm(request.POST)

    if(create_todo_form.is_valid()):
      todo = ToDo(description=create_todo_form.cleaned_data['todo'], completed=False)
      todo.save()
  
  create_todo_form = CreateTodoForm()

  todos = ToDo.objects.all()
  
  return render(request, "todo/list.html", {'todos': todos, 'create_todo_form': create_todo_form})
  #return HttpResponse("Hello, world!")

def delete(request, id):

  todo = ToDo.objects.filter(id=id)

  todo.delete()

  return redirect('/')

def check(request, id):
  todo = ToDo.objects.get(id=id)
  print(todo.description, todo.completed)

  todo.completed = not todo.completed
  todo.save()

  return redirect('/')