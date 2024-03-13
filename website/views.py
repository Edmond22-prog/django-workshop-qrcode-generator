from django.shortcuts import render

from website.models import DataInformation


def home(request):
    informations = DataInformation.objects.all().order_by("-created_at")
    context = {"informations": informations}
    return render(request, "website/index.html", context)


def generate_qrcode(request):
    if request.method == "GET":
        return render(request, "website/generate_qrcode.html")

    text_data = request.POST["text_data"]
    # Check if the data already exists
    try:
        data_information = DataInformation.objects.get(text_data=text_data)
        if data_information:
            context = {
                "text_data": data_information.text_data,
                "qr_code": data_information.qr_code.url,
            }
            return render(request, "website/generate_qrcode.html", context)

    except:
        # Create a new data information
        data_information = DataInformation.objects.create(text_data=text_data)
        context = {
            "text_data": data_information.text_data,
            "qr_code": data_information.qr_code.url,
        }
        return render(request, "website/generate_qrcode.html", context)

