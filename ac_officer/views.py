from django.shortcuts import render, redirect
from ac_citizen.models import Complaint

# Create your views here.
def officerComplaint(request):

    return render(request,"ac_officer/officer_complaint_menu.html")


def officerLogout(request):
    del request.session['off_un']
    del request.session['off_dept']
    return redirect('main_page')


def officerAssignedComplaints(request):
    department = request.session["off_dept"]
    qs = Complaint.objects.filter(department_id=department,status='assign')
    return render(request,"ac_officer/offiver_assigned_complaints.html",{"object_list":qs})

import datetime as dt
def officercloseComplaints(request):
    cid = request.GET.get("cid")
    td = dt.date.today()
    Complaint.objects.filter(cid=cid).update(status='closed',closedate=td)
    return redirect('officer_complaint')


def officerclosedComplaints(request):
    department = request.session["off_dept"]
    qs = Complaint.objects.filter(department_id=department, status='closed')
    return render(request, "ac_officer/officer_closed_complaints.html", {"object_list": qs})