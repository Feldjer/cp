from django.contrib import admin
from .models import *


class SubscriberAdmin (admin.ModelAdmin):
	#list_display = ["name", "email"]
	list_display = [field.name for field in Subscriber._meta.fields]
	fields = ["email"] # показываем, остальное исключаем
	#exclude = ["email"] - исключаем, отсальное показываем
	list_filter = ['name',]
	search_fields = ['name', 'email']
	
	class Meta:
		model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)

