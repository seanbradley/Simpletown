import re, requests, json
#from itertools import compress
#from operator import itemgetter, attrgetter

from django.contrib.auth.decorators import login_required
from django.contrib.flatpages.models import FlatPage
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import loader, Context, RequestContext
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView
from django.views.generic.base import View, TemplateView, TemplateResponse
from django.views.generic.detail import DetailView

from .models import Car
from .forms import CarForm


def dmv(request):

    if request.method == 'GET':  #<--change request.method to POST here, and in template
        form = CarForm(request.GET) #<--change request.method to POST here, and in template
        if form.is_valid():
            #data = form.data['vsn']  #<--uncomment
            data = request.GET.get("vsn")
            results = Car.objects.filter(vsn = data)
            #results = Car.objects.search("search_term_goes_here") # <--requires custom model manager
            context = {'results': results}
            return render_to_response(
            'cars/results.html',
            RequestContext(request, context)
            )

    else:
        form = CarForm()

    context = {'form': form}
    return render_to_response(
    'cars/dmv.html',
    RequestContext(request, context)
    )


'''
def results(request):
    context = {'results': results}
    return render_to_response(
    'cars/results.html',
    RequestContext(request, context)
    )
'''

'''
def dmv(request):

    if request.GET:
        form = CarSearchForm(request.GET)
        if form.is_valid():
            results = form.get_result_queryset()
        else:
            results = []
    else:
        form = CarSearchForm()
        results = []


    return render_to_response(
        'cars/dmv.html',
        RequestContext(request, {
            'form': form,
            'results': results,
        })
    )
'''

'''
# find and split search terms in the query
# omits spaces
def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


# return a combo of Django Q objects
# search for model keywords within given search fields
def get_query(query_string, search_fields):

    # search for every possible term
    query = None
    terms = normalize_query(query_string)

    # search for a given term in each field
    for term in terms:
        or_query = None
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query
'''

'''
@login_required
def dmv(request):
    query = request.GET['q']
    results = Car.objects.filter(vsn__icontains=query)
    template = loader.get_template()
    context = Context({ 'query': query, 'results':results })
    response = template.render(context)
    return HttpResponse(response)
'''

'''
results = BlogPost.objects.filter(Q(title__icontains=your_search_query) | Q(intro__icontains=your_search_query) | Q(content__icontains=your_search_query)).order_by('pub_date')

    #Generic Search: GET should contain the following:
    #terms - the search keywords separated by spaces
    terms = request.GET.get('terms', None)
    term_list = terms.split(' ')

    cars = Car.objects.all()

    q = Q(content__icontains=term_list[0]) | Q(title__icontains=term_list[0])
    for term in term_list[1:]:
        q.add((Q(content__icontains=term) | Q(title__icontains=term)), q.connector)

    cars = cars.filter(q)

    return render_to_response('cars/dmv.html', locals(), \
            context_instance=RequestContext(request))

'''

'''
    query_string = ''
    found_entries = None

    if ('q' in request.GET) and request.GET['q'].strip():

        query_string = request.GET['q']

        entry_query = get_query(query_string, ['title', 'body',])

        found_entries = Entry.objects.filter(entry_query).order_by('trim_id')

    context = {'query_string': query_string, 'found_entries': found_entries}

    return render_to_response(
        'cars/results.html',
        context,
        context_instance=RequestContext(request)
    )
'''


'''
class CarListView(ListView):
    model = Car

    def get_queryset(self):
        # Fetch the queryset from the parent get_queryset
        queryset = super(CarListView, self).get_queryset()

        # Get the q GET parameter
        q = self.request.GET.get("q")
        if q:
            # Return a filtered queryset
            return queryset.filter(vsn__icontains=q)

        # Return the base queryset
        return queryset
'''

