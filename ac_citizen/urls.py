"""ActiveCity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, ListView
from ac_admin.models import Department
from ac_citizen.models import Complaint

from ActiveCity import settings
from ac_citizen import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('citizen_index/',TemplateView.as_view(template_name="ac_citizen/citizen_index.html"), name="citizen_index"),
    path('citizen_register/',TemplateView.as_view(template_name="ac_citizen/citizen_register.html"),name="citizen_register"),
    path('citizen_save/',views.citizen_save,name="citizen_save"),
    path('citizen_otp_check/',views.citizen_otp_check,name='citizen_otp_check'),
    path('citizen_home/',TemplateView.as_view(template_name="ac_citizen/citizen_home.html"),name="citizen_home"),
    path('citizen_logout/',views.citizenLogout,name="citizen_logout"),
    path('citizen_complaint/',ListView.as_view(template_name="ac_citizen/citizen_complaint.html",model=Department),name="citizen_complaint"),
    path('citizen_complaint_register/',views.complaintRegister,name="citizen_complaint_register"),
    path('citizen_complaint_menu/',TemplateView.as_view(template_name="ac_citizen/citizen_complaint_menu.html"),name="citizen_complaint_menu"),
    path('citizen_pending_complaints/',ListView.as_view(template_name="ac_citizen/citizen_pending_complaints.html",model=Complaint,queryset=Complaint.objects.filter(status='pending')),name="citizen_pending_complaints"),
    path('citizen_assigned_complaints/',ListView.as_view(template_name="ac_citizen/citizen_assigned_complaints.html",model=Complaint,queryset=Complaint.objects.filter(status='assign')),name="citizen_assigned_complaints"),
    path('citizen_closed_complaints/',views.citizen_close_complaint,name="citizen_closed_complaints"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

