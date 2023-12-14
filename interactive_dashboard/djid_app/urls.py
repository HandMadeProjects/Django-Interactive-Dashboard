from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path('print_selected_topic/', views.print_selected_topic, name='print_selected_topic'),


    # path("load_data/", views.load_data, name="load_data"),


    # path("business", views.business, name="Business"),
    # path("about/", views.about, name="AboutUs"),
    # path("contact/", views.contact, name="ContactUs"),
    # path("products/<int:myid>", views.productView, name="ProductView"),
    # path("products/<str:myslug>", views.productView, name="ProductView"),

]