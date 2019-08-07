from django.shortcuts import render
from .models import Todo

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    due_date = request.GET.get('due-date')
   
    # 인스턴스를 만들고 나서 배정
    # todo = Todo()
    # todo.title = title
    # todo.content = content
    # todo.due_date = due_date
    # todo.save()

    todo = Todo(title=title, content=content, due_date=due_date)
    todo.save()

    return render(request, 'create.html')

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos,
    }
    return render(request, 'index.html', context)