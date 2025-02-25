from django.contrib import admin
from .models import User, Dictionary, Credit, Plan, Payment

admin.site.register(User)
admin.site.register(Dictionary)
admin.site.register(Credit)
admin.site.register(Plan)
admin.site.register(Payment)



