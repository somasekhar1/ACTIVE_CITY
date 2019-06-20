from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Department,Officer
from ac_login.models import Login
from ac_citizen.models import Complaint

def add_department(request):
    if request.method == "POST":
        d_name = request.POST.get("dept")
        qs1 = Department.objects.filter(name=d_name)

        if qs1:
            qs = Department.objects.all()
            return render(request, "ac_admin/admin_deparment.html", {"message": "Department is Available","object_list":qs})
        else:
            Department(name=d_name).save()
            qs = Department.objects.all()
            return render(request,"ac_admin/admin_deparment.html",{"object_list":qs})


def delete_department(request):
    dname = request.GET.get("name")
    res = Department.objects.filter(name=dname).delete()
    if res:
        qs = Department.objects.all()
        return render(request, "ac_admin/admin_deparment.html", {"object_list": qs,"message":"Department is Deleted"})


def update_department(request):
    d_name = request.GET.get("name")
    qs = Department.objects.all()
    return render(request, "ac_admin/admin_deparment.html", {"object_list": qs, "dname": d_name})



def update1_department(request):
    new_dname = request.POST.get("dept")
    old_dname = request.POST.get("dept1")
    Department.objects.filter(name=old_dname).update(name=new_dname)
    qs = Department.objects.all()
    return render(request, "ac_admin/admin_deparment.html", {"object_list": qs, "message": "Department Updated"})


def admin_officer(request):
    qs = Department.objects.all()
    qs1 = Officer.objects.all()
    return render(request,"ac_admin/admin_officer.html",{"dept_data":qs,"officer_data":qs1})


def add_officer(request):
    if request.method == "POST":
        idno = request.POST.get("idno")
        name = request.POST.get("name")
        department = request.POST.get("dept")
        contact = request.POST.get("contact")
        image = request.FILES["image"]
        username = request.POST.get("username")
        password = request.POST.get("password")

        message = sendACASMS(contact)
        import json
        d1 = json.loads(message)
        if d1["return"]:
            Login(username=username,password=password,usertype="officer").save()
            Officer(idno=idno,name=name,deparment_id=department,contact=contact,image=image,username_id=username).save()
            qs = Department.objects.all()
            qs1 = Officer.objects.all()
            return render(request,"ac_admin/admin_officer.html",{"message":"Registered","dept_data":qs,"officer_data":qs1})
        else:
            qs = Department.objects.all()
            qs1 = Officer.objects.all()
            return render(request, "ac_admin/admin_officer.html",
                          {"message": "Invalid Contact No", "dept_data": qs, "officer_data": qs1})


def sendACASMS(contactno):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=Hello Officer You have been Registread to Active City Application &language=english&route=p&numbers="+contactno
    headers = {
        'authorization': "OmgfGSeqd49CbLrTwUAN0MPJxyt3ZE1l7FV2RDcv58uKjhaXnBymtEP9Agv2q3VscNwIDiQaronejlZM",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text


def admin_assign_complaint(request):
    cid = request.GET.get("cid")
    Complaint.objects.filter(cid=cid).update(status='assign')
    return redirect('admin_complaint_menu')


def admin_closed_complaint(request):
    qs = Complaint.objects.filter(status='closed')
    return render(request,"ac_admin/admin_closed_complaints.html",{"object_list":qs})