from django.shortcuts import render,get_object_or_404,redirect
from .models import Invoice,InvoiceItem,InvoiceBillSundry

# Create your views here.
def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request,'invoiceapp/invoice_list.html',{'invoices':invoices})

def invoice_detail(request,id=None):
    if id :
        invoice = get_object_or_404(Invoice,pk=id)
    else :
        invoice = Invoice()
    if request.method =='Post':
        pass
    return render(request,'invoiceapp/invoice_detail.html',{'invoice':invoice})
    