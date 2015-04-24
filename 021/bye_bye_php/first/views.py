from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def start_here(request):
    return HttpResponse('<h1>Are we there yet</h1>')
    
def distance(request):
    from_city = request.GET.get('from', 'Your Location')
    to_city = request.GET.get('to', 'Destination')
    
    template = loader.get_template('first/distance.html')
    
    if from_city == 'Hyderabad' and to_city == 'Vijayawada':
        distance = 'Infinity and Beyond'
    else:
        distance = 'In the digital age, it takes 0 seconds'
    
    context = RequestContext(request, {
            'starting_point': from_city,
            'destination': to_city,
            'time_to_reach': distance
    })
    return HttpResponse(template.render(context))
    