import re, requests, json
#from itertools import compress
#from operator import itemgetter, attrgetter

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import loader, Context, RequestContext
#from django.db.models import Q
#from django.views.generic import ListView


from .models import Car
from .forms import CarForm

@login_required
def dmv(request):

    if 'submit' in request.GET:
        form = CarForm(request.GET)
        if form.is_valid():
            data = request.GET.get("vsn")
            results = Car.objects.filter(vsn = data)
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
# Follows are some ideas about refactoring the above...

# use a queryset...
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


# filter results with icontains...
def dmv(request):
    query = request.GET['q']
    results = Car.objects.filter(vsn__icontains=query)
    template = loader.get_template()
    context = Context({ 'query': query, 'results':results })
    response = template.render(context)


# incorporate a utility function to find and split search terms and omit
# spaces in the query...
def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


# use Django Q objects (or a combo of them) to search via model keywords
# within given search fields...
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


# chain together Django Q objects  via OR or AND to make more precise queries...
results = Car.objects.filter(Q(vsn__icontains=query) | Q(some_other_model_attirbute__icontains=query)

    #Generic Search: GET should contain the following:
    #terms - the search keywords separated by spaces
    terms = request.GET.get('terms', None)
    term_list = terms.split(' ')

    cars = Car.objects.all()

    q = Q(vsn__icontains=term_list[0]) | Q(some_other_model_attribute__icontains=term_list[0])
    for term in term_list[1:]:
        q.add((Q(vsn__icontains=term) | Q(some_other_model_attribute__icontains=term)), q.connector)

    cars = cars.filter(q)

    return render_to_response('cars/dmv.html', locals(), \
            context_instance=RequestContext(request))


# another refactoring: enables search via multiple model attributes...

    query_string = ''
    found_entries = None

    if ('q' in request.GET) and request.GET['q'].strip():

        query_string = request.GET['q']
        vsn_query = get_query(query_string, ['a_model_attribute', 'another_model_attribute',])
        results = Entry.objects.filter(vsn_query).order_by('trim_id')

    context = {'query_string': query_string, 'results': results}

    return render_to_response(
        'cars/results.html',
        context,
        context_instance=RequestContext(request)
    )


# or, finally, use as a class-based view...
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

