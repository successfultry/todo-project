from django.shortcuts import render
from django.http import (HttpResponse, HttpRequest)
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.
from .models import ToDoItem


def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = ToDoItem.objects.order_by('id').all()[0:2]
    return render(
        request,
        template_name="todo_list/index.html",
        context={"todo_items": todo_items}
    )


class ToDoListIndexView(ListView):
    template_name = "todo_list/index.html"
    queryset = ToDoItem.objects.all()[0:2]
    # model = ToDoItem
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["todo_items"] = ToDoItem.objects.all()
    #     return context


class ToDoListView(ListView):
    # template_name = "todo_list/index.html"
    model = ToDoItem
    # context_object_name = "todo_items"


class ToDoListDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all()


class ToDoDetailView(DetailView):
    model = ToDoItem
