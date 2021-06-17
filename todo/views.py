from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from .models import TodoList, TodoList_files, TodoList_images 
from django.views import generic 
from .forms import TodoCreateForm
from datetime import datetime

# Create your views here. 

class IndexView(generic.ListView):
    context_object_name = 'to_do_list'
    template_name = 'todo/todolist_list.html'
    # template_name = 'todo/list.html'
    
    def get_queryset(self):
        # return TodoList.objects.all()
        return TodoList.objects.order_by('date_deadline')

class DetailView(generic.DetailView):
    model = TodoList
    contxt_object_name = 'todolist'
    template_name = 'todo/todolist_detail.html'
    # tempalte_name = 'todo/detail.html'
    
    def get_queryset(self):
        return TodoList.objects.all()

class DeleteView(generic.DeleteView):
    model = TodoList 
    success_url = '/todo'
    tempalte_name = 'todo/todolist_delete.html'
    # tempalte_name = 'todo/delete.html'

class UpdateView(generic.UpdateView):
    model = TodoList 
    fields = ['name', 'description', 'date_deadline']
    template_name = 'todo/todolist_update.html'
    # template_name = 'todo/update.html'
    success_url = "/todo"

def TodoCreate(request):
    if request.method == "POST":
        form = TodoCreateForm(request.POST)
        
        name = request.POST['name']
        description = request.POST['description']
        date_deadline = request.POST['date_deadline']
        images = request.FILES.getlist('images')
        files = request.FILES.getlist('files')
        date_created = datetime.today()
        
        # valid 한 date_deadline value 를 넣지 않았을때 막을 방법이 없음.
        # date_created 가 date_deadline 보다 지난 날짜라도, Todo는 생성되는 문제점도 있음 
        
        t = TodoList.objects.create(
        	name=name,
        	description=description,
        	date_created=date_created,
        	date_deadline=date_deadline,
        )
        
        t.save()
        
        for image in images:
            TodoList_images.objects.create(todo=t, image=image)
            
        for file_in_list in files:
            TodoList_files.objects.create(todo=t, files=file_in_list)
            
        return redirect('/todo')
    
    else:
        form = TodoCreateForm()
        return render(request, 'todo/todolist_create.html', {'form': form})