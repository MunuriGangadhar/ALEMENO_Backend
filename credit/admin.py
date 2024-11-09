from django.contrib import admin
from .models import Customer, Loan

# Register the models with default settings
admin.site.register(Customer)
admin.site.register(Loan)
