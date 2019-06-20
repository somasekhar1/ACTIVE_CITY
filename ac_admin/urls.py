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
from django.views.generic import TemplateView, CreateView, ListView

from ActiveCity import settings
from ac_admin import views
from ac_admin.models import Department,Officer
from ac_citizen.models import Complaint

urlpatterns = [
    path('admin_index/',TemplateView.as_view(template_name='ac_admin/admin_index.html'),name="admin_index" ),
    path('admin_home/',TemplateView.as_view(template_name="ac_admin/admin_home.html"),name="admin_home"),
        # admin department
    path('admin_department/',ListView.as_view(model=Department,template_name="ac_admin/admin_deparment.html"),name="admin_department"),
    path('save_depatment/',views.add_department,name="admin_save_department"),
    path('delete_depatment/',views.delete_department,name="admin_delete_department"),
    path('update_depatment/',views.update_department,name="admin_update_department"),
    path('update1_depatment/',views.update1_department,name="admin_update1_department"),

    # admin Officer
    path('admin_officer/',views.admin_officer,name="admin_officer"),
    path('save_officer/',views.add_officer,name="admin_save_officer"),

    # admin complaint
    path('admin_complaint_menu/',TemplateView.as_view(template_name="ac_admin/admin_complaint_menu.html"),name="admin_complaint_menu"),
    path('admin_pending_complaints/',ListView.as_view(template_name="ac_admin/admin_pending_complaints.html",model=Complaint,queryset=Complaint.objects.filter(status='pending')),name="admin_pending_complaints"),
    path('admin_assigned_complaints/',ListView.as_view(template_name="ac_admin/admin_assigned_complaints.html",model=Complaint,queryset=Complaint.objects.filter(status='assign')),name="admin_assigned_complaints"),
    path('admin_assign_complaint/',views.admin_assign_complaint,name="admin_assign_complaint"),
    path('admin_closed_complaint/',views.admin_closed_complaint,name="admin_closed_complaints"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

