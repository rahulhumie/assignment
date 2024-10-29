from django.urls import path
from .views import invoice_list,invoice_detail
urlpatterns =[path('invoices/',invoice_list,name='invoice_list'),
              path('invoice/<int:id>/', invoice_detail,name = 'invoice_detail'),
              path('invoice/new/',invoice_detail,name='invoice_new'),
              
              ]
