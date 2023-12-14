#  i have created this file - GTA
from django.shortcuts import render, redirect
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
    allDashboardData = DashboardData.objects.all()

    # Get all unique topics from the DashboardData model
    unique_topics = DashboardData.objects.values_list('topic', flat=True).distinct()

    # Convert QuerySet to a list for easier handling in the template
    unique_topics_list = list(unique_topics)


    params = {
    # 'catproducts' : all_prods,
    'selected_data' : allDashboardData,
    'unique_topics_list' : unique_topics_list,
            }


    # return HttpResponse(f'djid_app    | {jsonFilePath}')
    return render(request,'djid_app/index.html', params)

def print_selected_topic(request):
    if request.method == 'POST':
        selected_topics = request.POST.getlist('selected_topics')
        print(f"Selected Topics: {selected_topics}")

        unique_topics = DashboardData.objects.values_list('topic', flat=True).distinct()
        unique_topics_list = list(unique_topics)

        
        selected_data = DashboardData.objects.filter(topic=selected_topics[0])
        
        params = {
        # 'catproducts' : all_prods,
        'selected_data' : selected_data,
        'unique_topics_list' : unique_topics_list,
                }
        return render(request, 'djid_app/index.html', params)
    
    return redirect("index")

    # return HttpResponse("Selected topics printed in the terminal.")
    # return render(request,'djid_app/index.html', params)







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
