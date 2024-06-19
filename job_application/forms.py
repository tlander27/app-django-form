from django import forms


class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    position = forms.CharField(max_length=50)
    status = forms.CharField(max_length=50)
    start_date = forms.DateField()

