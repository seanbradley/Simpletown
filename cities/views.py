from django.shortcuts import render, get_object_or_404

from cities.models import City

def view_one(request):
    list_everything = []
    context = {'list_everything': list_everything}
    return render(request, 'cities/view_one.html', context)
    
def view_two(request):
    list_by_county = []
    context = {'list_by_county': list_by_county}
    return render(request, 'cities/view_two.html', context)
