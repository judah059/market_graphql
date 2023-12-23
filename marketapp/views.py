from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.template.loader import render_to_string

from marketapp.models import ProductCategory


def add_ajax(request):
    data = request.GET.get('data')
    if data:
        categories = ProductCategory.objects.filter(
            shops=data
        )
        context = {
            'product_categories': categories
        }
        rendered = render_to_string('category_list.html', context)
        response = {'html': rendered}
        return JsonResponse(response)
    raise Http404
