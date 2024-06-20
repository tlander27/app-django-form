from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.files.storage import default_storage


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        print(type(form))
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            position = form.cleaned_data["position"]
            status = form.cleaned_data["status"]
            start_date = form.cleaned_data["start_date"]
            # new_file = Form(file=request.FILES['file'])
            new_file = request.FILES['file']
            default_storage.save(new_file.name, new_file)

            print(form.cleaned_data)

            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                position=position,
                status=status,
                start_date=start_date,
                file=new_file.name,
            )

            message_body = f"Hello, {first_name},\n" \
                f"Thank you for applying for the {position} position. " \
                "Our team with review your qualifications and be in touch.\n\n" \
                "Submitted information:\n\n" \
                f"Name: {first_name} {last_name}\n" \
                f"Email: {email}\n" \
                f"Position: {position}\n" \
                f"Start Date: {start_date}\n" \
                f"Employment Status: {status}\n" \
                f"Resume: {new_file.name}\n\n" \
                "Thank you,\n\n" \
                "-Hiring Team"

            email_message = EmailMessage(
                subject="Application Confirmation",
                body=message_body,
                to=[email],
                from_email="DEV_44 HR"
            )
            email_message.send()

            messages.success(request, f"Thank you, {first_name}! Your application has been submitted!")

    return render(request, "index.html")


def about(request):
    return render(request, 'about.html')