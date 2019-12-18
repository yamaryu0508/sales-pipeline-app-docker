from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from .filters import ItemFilterSet
from .forms import ItemForm
from .models import Item

class ItemFilterView(LoginRequiredMixin, FilterView):
    """
    Index view
    filtering by https://django-filter.readthedocs.io/en/master/
    """
    model = Item

    filterset_class = ItemFilterSet
    strict = False

    # show p1
    paginate_by = 10

    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)

    def get_queryset(self):
        return Item.objects.all().order_by('-created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(object_list=object_list, **kwargs)


class ItemDetailView(LoginRequiredMixin, DetailView):
    """
    Detail view
    """
    model = Item

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ItemCreateView(LoginRequiredMixin, CreateView):
    """
    Create view
    """
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        item = form.save(commit=False)
        item.created_by = self.request.user
        item.created_at = timezone.now()
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        return HttpResponseRedirect(self.success_url)


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update view
    """
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        item = form.save(commit=False)
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        return HttpResponseRedirect(self.success_url)


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete view
    """
    model = Item
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        item = self.get_object()
        item.delete()

        return HttpResponseRedirect(self.success_url)
