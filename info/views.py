from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import AboutUs, ContactUs
from .forms import ContactForm
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def AboutUsView(request):
    content = AboutUs.objects.all()
    context = {
        'content': content
    }
    return render(request, 'aboutus.html', context)


class ContactUsView(View):
    def get(self, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(self.request, 'contactus.html', context)

    def post(self, *args, **kwargs):
        form = ContactForm(self.request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phoneNo = form.cleaned_data.get('phoneNumber')
            message = form.cleaned_data.get('message')
            print(name, email, phoneNo, message)

            try:
                contact = ContactUs()
                contact.name = name
                contact.email = email
                contact.phoneNo = phoneNo
                contact.message = message
                contact.save()
                messages.info(self.request, 'Thank you for Contacting us, We will respond shortly')
                return redirect('/')
            except ObjectDoesNotExist:
                messages.info(self.request, 'Uhhhn, Something went wrong, please try again.')
                return redirect('/')


# class ContactUsView(View):
#     def  get(self, *args, **kwargs):
#         form = ContactForm()
#         context = {
#              'form': form}  
#         return render(self.request, 'contactus.html', context)


#     def post(self, *args, **kwargs):
#         form = ContactForm(self.request.POST)
#         if form.is_valid():
#             name = form.cleaned_data.get('name')
#             email = form.cleaned_data.get('email')
#             phoneNumber = form.cleaned_data.get('phoneNumber')
#             message = form.cleaned_data.get('message')
#             # edit order
#             try:
#                 order = Order.objects.get(ref_code=ref_code)
#                 order.refund_requested = True
#                 order.save()
            

#                 # store the refund
#                 refund = ContactForm()
#                 refund.order = order
#                 refund.reason = message
#                 refund.email = email
#                 refund.save()

#                 messages.info(self.request, 'Your request was recieved')
#                 return redirect('core:request-refund')
                
#             except ObjectDoesNotExist:
#                 messages.info(self.request, 'This order does not exist')
#                 return redirect('core:request-refund')