from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.management_fund_dashboard,
        name='management_fund_dashboard'
    ),

]