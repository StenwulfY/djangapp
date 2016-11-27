from django.contrib import admin

# Register your models here.
 
# - Import Question
from .models import Question, Choice
# - Register Question for showing in admin
admin.site.register(Question)

admin.site.register(Choice)