from django.shortcuts import render


def index_view(request):
    return render(request,'website/index.html')


def about_view(request):
    context = {"title":"I'm Hamed, a Python developer specializing in the design, development, and deployment of various types of websites."}
    return render(request, "website/about.html", context)


def contact_view(request):
    return render(request, "website/contact.html")


def portfolio_view(request):
    return render(request, "website/portfolio.html")


def portfolio_details_view(request):
    return render(request, "website/portfolio-details.html")


def resume_view(request):
    return render(request, "website/resume.html")


def service_view(request):
    return render(request, "website/services.html")


def service_details_view(request):
    return render(request, "website/service-details.html")


def starter_page(request):
    return render(request, "website/starter-page.html")
