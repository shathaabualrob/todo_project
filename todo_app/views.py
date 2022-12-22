from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView
from .models import ToDoList, ToDoItem

class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"

class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id = self.kwargs['list_id'])

    def get_context_data(self):
        context = super().get_context_data()
        context['todo_list'] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context

class ListCreateView(CreateView):
    model = ToDoList
    fields = {"title"}

    def get_context_data(self):
        context = super(ListCreateView, self).get_context_data()
        context["title"] = "Add a new List"
        return context

class ItemCreateView(CreateView):
    model = ToDoItem
    fields = {
        "title",
        "description",
        "created_date",
        "due_date",
        }

    # def get_initial(self):
    #     return self.
    


   