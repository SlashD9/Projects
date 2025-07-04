from django.urls import path
from .views import home, sites, worksheet, service, customer, stock
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

admin.site.site_header = 'Worksheets'                    # default: "Django Administration"
admin.site.index_title = 'Selection Area'                 # default: "Site administration"
admin.site.site_title = 'Worksheets' # default: "Django site admin"

app_name = 'accounts'


urlpatterns = [
    path("accounts/login/", auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('', sites, name='Sites'),
    
    path('sites/', sites, name='Sites'),
    path('sites/add_site/', views.add_site, name="add_site"),
    path('sites/edit_site/<id>', views.edit_site, name="edit_site"),
    path('sites/delete_site/<id>', views.delete_site, name="delete_site"),

    path('customer/', customer, name='Customer'),
    path('customer/add_customer/', views.add_customer, name="add_customer"),
    path('customer/edit_customer/<id>', views.edit_customer, name="edit_customer"),
    path('customer/delete_customer/<id>', views.delete_customer, name="delete_customer"),

    path('worksheet/', worksheet, name='Worksheet'),
    path('worksheet/add_worksheet/', views.add_worksheet, name="add_worksheet"),
    path('worksheet/edit_worksheet/<id>', views.edit_worksheet, name="edit_worksheet"),
    path('worksheet/delete_worksheet/<id>', views.delete_worksheet, name="delete_worksheet"),

    path('service/', service, name='Service Sheet'),
    path('service/add_service/', views.add_service, name="add_service"),
    path('service/edit_service/<id>', views.edit_service, name="edit_service"),
    path('service/delete_service/<id>', views.delete_service, name="delete_service"),

    path('stock/', stock, name='Stock Sheet'),
    path('stock/add_stock/', views.add_stock, name="add_stock"),
    path('stock/edit_stock/<id>', views.edit_stock, name="edit_stock"),
    path('stock/delete_stock/<id>', views.delete_stock, name="delete_stock"),
    
    
]

