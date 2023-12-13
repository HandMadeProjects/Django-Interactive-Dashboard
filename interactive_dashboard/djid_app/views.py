#  i have created this file - GTA
from django.shortcuts import render
from django.http import HttpResponse
from .models import DashboardData
# import random


# import json
from django.core.exceptions import ValidationError
from datetime import datetime

import os
from django.conf import settings
jsonFilePath = os.path.join(settings.SERVERDATA_ROOT, 'djid_app\jsondata.json')


# Create your views here.

def index(request):
    # return HttpResponse(f'djid_app    | {jsonFilePath}')
    return render(request,'djid_app/index.html')








# -------------------------- Modules --------------------------
def convert_to_datetime(date_string):
    try:
        # Define the format of the date string
        date_format = "%B, %d %Y %H:%M:%S"
        
        # Parse the date string using the defined format
        datetime_object = datetime.strptime(date_string, date_format)
        
        return datetime_object
    except ValueError as e:
        # Handle the case where the date string doesn't match the specified format
        print(f"____Error: {e}")
        # print(f"\n\t\t\t\t\t\tError in this string: {date_string}")
        return None





# ===================================================== Example ===================================================== 

# def index(request):
#     products = Product.objects.all()

#     all_prods = []
#     catProds = Product.objects.values('category', 'Product_id')
#     cats = {item['category'] for item in catProds}
#     for cat in cats:
#         prod = Product.objects.filter(category=cat)
#         n = len(products)
#         all_prods.append([prod, n]) 

#     params = {
#         'catproducts' : all_prods,
#         'allproducts' : products,
#               }

#     return render(request,'tze/index.html', params)


# def business(request):
#     # return HttpResponse('Teamzeffort    |      business Page')
#     return render(request,'tze/business.html')

# def about(request):
#     return render(request,'tze/about.html')

# def contact(request):
#     coreMem = Contact.objects.filter(mem_tag="core")
#     teamMem = Contact.objects.filter(mem_tag="team")
#     # print(f"coreMem: {coreMem} \n teamMem: {teamMem}")

#     return render(request, 'tze/contact.html', {'core':coreMem,'team':teamMem })

# def productView(request, myslug):
#     # Fetch the product using the id
#     product = Product.objects.filter(slug=myslug)
#     prodCat = product[0].category
#     # print(prodCat)
#     recproduct = Product.objects.filter(category=prodCat)
#     # print(recproduct)

#     # randomObjects = random.sample(recproduct, 2)
#     randomObjects = random.sample(list(recproduct), 2)


#     return render(request, 'tze/prodView.html', {'product':product[0],'recprod':randomObjects })


# def index(request):
#     return HttpResponse('Teamzeffort    |      index Page')
