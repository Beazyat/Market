from django.shortcuts import get_object_or_404, render

from .models import Item, Category


# Create your views here.
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
