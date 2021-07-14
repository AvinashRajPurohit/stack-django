import requests
import requests_cache
from django.shortcuts import render
import json
from ratelimit.decorators import ratelimit
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from stack_search.forms import StackSearchForm

requests_cache.install_cache('stack_search_cache', backend='sqlite', expire_after=180)


def return_data(data):
    cleaned_data = dict()
    for k, v in data.items():
        if k == 'csrfmiddlewaretoken' or k == 'is_search':
            continue
        else:
            cleaned_data[k] = v
    cleaned_data['site'] = "stackoverflow"
    return cleaned_data


@ratelimit(key='ip', rate='5/m')
@ratelimit(key='ip', rate='100/d')
def stack_search(request):
    page = request.GET.get('page', 1)
    params = return_data(request.GET)
    if request.GET.get('is_search', '') == 'search_data':
        endpoint = 'https://api.stackexchange.com/2.2/search/advanced'
        response = requests.get(url=endpoint, params=params)
        if response.status_code == 200:
            data = json.loads(response.text)['items']
            paginator = Paginator(data, 5)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)

            context = {
                'data': data,
                'is_data': True,
                'form': StackSearchForm,
                'max': max(list(data.paginator.page_range)),
                'q': request.GET.get('q')
            }
            return render(request, 'stack_search/home.html', context)
    context = {
        'form': StackSearchForm,
    }
    return render(request, 'stack_search/home.html', context)

