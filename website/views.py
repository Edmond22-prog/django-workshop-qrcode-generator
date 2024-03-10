import json

from django.shortcuts import render

from website.forms import RegisterEmployeeForm
from website.models import Employee
from website.utils import generate_qr_code


def home(request):
    return render(request, "website/index.html")


def register_employee(request):
    if request.method == "GET":
        return render(request, "website/register_employee.html")

    else:
        form = RegisterEmployeeForm(request.POST)
        if form.is_valid():
            # Create a new employee
            fullname = form.cleaned_data["fullname"]
            email = form.cleaned_data["email"]
            department = form.cleaned_data["department"]
            employee = Employee.objects.create(
                fullname=fullname, email=email, department=department
            )
            
            context_data = {
                "fullname": employee.fullname,
                "email": employee.email,
                "department": employee.department,
            }
            # dumped_data = json.dumps(context_data)
            # qr_code_img = generate_qr_code(dumped_data)
            # employee.qr_code = qr_code_img
            # employee.save()
            
            # context_data["qr_code"] = employee.qr_code.url
            # context_data["registered"] = True
            
            return render(request, "website/register_employee.html", context_data)
