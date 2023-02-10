from django.contrib import admin
from .models import*

admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Receipt)
