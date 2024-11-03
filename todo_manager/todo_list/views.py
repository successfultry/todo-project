from django.shortcuts import render
from django.http import (HttpResponse, HttpRequest, HttpResponseRedirect)
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from .models import ToDoItem
from .forms import ToDoItemCreateForm, ToDoItemUpdateForm

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
    # model = ToDoItem
    queryset = ToDoItem.objects.filter(archived=False).all()



class ToDoListDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all()


class ToDoDetailView(DetailView):
    # model = ToDoItem
    queryset = ToDoItem.objects.filter(archived=False)


class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoItemCreateForm


class ToDoItemUpdateView(UpdateView):
    model = ToDoItem
    template_name_suffix = "_update_form"
    form_class = ToDoItemUpdateForm


class ToDoItemDeleteView(DeleteView):
    model = ToDoItem
    success_url = reverse_lazy("todo_list:list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)