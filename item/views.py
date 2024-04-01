from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from .models import Item, Category
from .forms import NewItemForm, UpdateItemForm


class CreateNewItemView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = 'create_new_item.html'
    form_class = NewItemForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    # check form is valid and next add created_by field to item.

    def get_success_url(self):
        new_item = self.object  # You can use any variable name here
        return reverse_lazy('detail', kwargs={'pk': new_item.pk})
    # if add item is successed, redirect user to item detail page.

# @login_required
# def new_item(request):
#     if request.method == "POST":
#         form = NewItemForm(request.POST, request.FILES)

#         if form.is_valid():
#             item = form.save(commit=False)
#             item.created_by = request.user
#             item.save()
#             return redirect("detail", pk=item.id)
#     else:
#         form = NewItemForm()
    
#     context = {
#         'form': form ,
#     }
#     return render(request, "create_new_item.html", context)


def detail(request, pk):
    """
    View function for a detail page of an item.

    :param request: The incoming request.
    :type request: HttpRequest
    :param pk: The primary key of the item to retrieve.
    :type pk: int
    :return: The rendered template with the item and related items.
    :rtype: HttpResponse
    """
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(
        category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    context = {
        'item': item,
        'related_items': related_items,
        }
    return render(request, 'detail.html', context)


class DeleteItem(LoginRequiredMixin, DeleteView):
    model = Item
    fields = '__all__'
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy("dashboard")


class UpdateItem(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = 'edit.html'
    form_class = UpdateItemForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        item = self.object
        return reverse_lazy("detail", kwargs={'pk': item.id})