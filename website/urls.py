from django.urls import path
from website.views import *
app_name = "website"

urlpatterns = [
    path("", index_view, name="index"),

    path("about", about_view, name="about"),

    path("contact", contact_view, name="contact"),

    path("resume", resume_view, name="resume"),

    path("portfolio-details", portfolio_details_view, name="portfolio-details"),
    path("portfolio", portfolio_view, name="portfolio"),
    path("service-details", service_details_view, name="Service-details"),
    path("service", service_view, name="service"),
    path("starter-page",starter_page, name="starter-page"),
]
