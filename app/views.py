from django.http import JsonResponse
from smtplib import SMTPException
from django.shortcuts import render
from django.views.generic.base import View
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, BadHeaderError
from smtplib import SMTPException
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.views import APIView



from .forms import ContactForm

# Create your views here.

class LandingPageView(View):
    template_name = "index.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)
    

class AboutPageView(View):
    template_name = "about.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)
    


class ContactPageView(View):
    template_name = "contact.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        return render(request, self.template_name)


    # def post(self, request):
        # form = ContactForm(request.POST)
        # if form.is_valid():
        #     fullname = form.cleaned_data["fullname"]
        #     email = form.cleaned_data["email"]
        #     subject = form.cleaned_data["subject"]
        #     message = form.cleaned_data["message"]

        #     # Prepare the HTML and plain text versions of the message
        #     html_message = render_to_string('email_template.html', {'fullname': fullname, 'email': email, 'message': message})
        #     plain_message = strip_tags(html_message)

        #     try:
        #         send_mail(subject, plain_message, 'info@gakaliztravelsandtour.com', ['info@gakaliztravelsandtour.com'], html_message=html_message)
        #         return JsonResponse({'success': True, 'message': 'Your message has been sent. Thank you!'})
        #     except BadHeaderError as e:
        #         # Handle BadHeaderError
        #         error_message = str(e)
        #         return JsonResponse({'success': False, 'message': 'Failed to send email. Please try again later.', 'error': error_message})
        #     except SMTPException as e:
        #         # Handle SMTP errors
        #         error_message = str(e)
        #         return JsonResponse({'success': False, 'message': 'Failed to send email. Please try again later.', 'error': error_message})
        # else:
        #     errors = form.errors.as_json()
        #     print(errors)
        #     return JsonResponse({'success': False, 'errors': errors})


# endpoints

class ContactAPiView(APIView):

    def post(self, request):
        form = ContactForm(request.POST)
        print(form, 'innder')
        if form.is_valid():
            fullname = form.cleaned_data["fullname"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            # Prepare the HTML and plain text versions of the message
            html_message = render_to_string('email_template.html', {'fullname': fullname, 'email': email, 'message': message})
            plain_message = strip_tags(html_message)

            try:
                send_mail(subject, plain_message, 'info@gakaliztravelsandtour.com', ['info@gakaliztravelsandtour.com'], html_message=html_message)
                return JsonResponse({'success': True, 'message': 'Your message has been sent. Thank you!'})
            except BadHeaderError as e:
                # Handle BadHeaderError
                error_message = str(e)
                return JsonResponse({'success': False, 'message': 'Failed to send email. Please try again later.', 'error': error_message})
            except SMTPException as e:
                # Handle SMTP errors
                error_message = str(e)
                return JsonResponse({'success': False, 'message': 'Failed to send email. Please try again later.', 'error': error_message})
        else:
            errors = form.errors.as_json()
            print(errors)
            return JsonResponse({'success': False, 'errors': errors})
