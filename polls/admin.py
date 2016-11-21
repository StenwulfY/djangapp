from django.contrib import admin

# Register your models here.
 
# - Import Question
from .models import Question
# - Register Question for showing in admin
admin.site.register(Question)