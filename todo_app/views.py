from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_app.forms import TagForm, TaskForm
from todo_app.models import Tag, Task


def index(request):
    """View function for the home page of the site."""
    tasks = (
        Task.objects.prefetch_related("tags").order_by("-is_done")
    )

    # paginator = Paginator(tasks, 5)
    # page_number = request.GET.get("page")
    #
    # try:
    #     posts = paginator.page(page_number)
    # except PageNotAnInteger:
    #     posts = paginator.page(1)
    # except EmptyPage:
    #     posts = paginator.page(paginator.num_pages)

    context = {
        "task_list": tasks,
    }
    return render(request, "todo/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5
    template_name = "todo/tag_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        # name = self.request.GET.get("name", "")
        # context["search_form"] = TagSearchForm(initial={"name": name})
        return context

    # def get_queryset(self):
    #     form = TagSearchForm(self.request.GET)
    #     queryset = Tag.objects.all()
    #     if form.is_valid():
    #         return queryset.filter(name__icontains=form.cleaned_data["name"])
    #     return queryset


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:index")


def change_task_status(request, pk):
    task = Task.objects.get(pk=pk)
    if task.is_done:
        task.is_done = False
    else:
        task.is_done = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:index"))
