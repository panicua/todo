from django.shortcuts import render
from django.views import generic

from todo_app.models import Tag


def index(request):
    context = {}
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
