from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            position = form.cleaned_data["position"]
            start_date = form.cleaned_data["start_date"]
            status = form.cleaned_data["status"]

            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                position=position,
                start_date=start_date,
                status=status
            )

            messages.success(request, f"Thank you, {first_name}! Your application has been submitted!")

    return render(request, "index.html")