from django.db import models

# Create your models here.
class Invoice(models.Model):
    invoice_number = models.AuthField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    billing_address = models.TextField()
    shipping_address = models.TextField()
    gstin = models.CharField(max_length=15)
    total_amount = models.DecimalField(max_digit = 10, decimal_places= 2)
class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice,related_name ='items',on_delete=models.CASCADE)
    item_name= models.CharField(max_length=255)
    quantity = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digit=10,decimal_place=2)
    amount = models.DecimalField(max_digit=10,decimal_place=2)

class InvoiceBillSundry(models.Model):
    invoice = models.ForeignKey(Invoice,related_name = 'bill_sundries',on_delete = models.CASCADE)
    bill_sundry_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digit =10 , decimal_places =2)