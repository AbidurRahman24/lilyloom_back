from django.contrib import admin
from . import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['flower', 'name']
    def name(self,obj):
        return obj.user.first_name
    
    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.status == "Completed":
            email_subject = "Your Order is Completed"
            email_body = render_to_string('admin_email.html', {'user' : obj.user, 'product' : obj.flower})
            
            email = EmailMultiAlternatives(email_subject , '', to=[obj.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

admin.site.register(models.Order, OrderAdmin)
