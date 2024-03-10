from django import forms


class RegisterEmployeeForm(forms.Form):
    fullname = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    department = forms.ChoiceField(
        choices=[("IT", "It"), ("HR", "Hr"), ("Finance", "Finance")],
        required=True,
    )
