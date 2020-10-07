from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing, SiteMetaData
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    metadata = SiteMetaData.objects.all()
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        "desc1": SiteMetaData.objects.get().desc1,
        "desc2": SiteMetaData.objects.get().desc2,
        "desc3": SiteMetaData.objects.get().desc2,
        "desc4": SiteMetaData.objects.get().desc4,
        "title": SiteMetaData.objects.get().meta_title,
        "location": SiteMetaData.objects.get().location,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
