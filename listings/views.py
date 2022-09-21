from django.shortcuts import render
from .models import Listing

# Create your views here.

# CURD -> Create, Retrieve, Update, Delete, List


def listing_list(request):
    listings = Listing.objects.all()

    context = {
        "listings": listings
    }

    return render(request, "listings.html", context)


def listing_retrieve(request, id):
    listing = Listing.objects.get(id=id)
    context = {
        "listing": listing
    }
    return render(request, "listings.html", context)
