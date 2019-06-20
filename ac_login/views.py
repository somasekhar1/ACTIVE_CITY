from django.http import HttpResponse
from django.shortcuts import redirect
from ac_login.models import Login
from ac_citizen.models import CitizenRegister
from ac_admin.models import Officer
from django.contrib import messages


def loginCheck(request):
    un = request.POST.get("username")
    up = request.POST.get("password")
    utype = request.POST.get("utype")

    qs = Login.objects.filter(username=un,password=up,usertype=utype)
    if qs:
        if utype == "admin":
            return redirect('admin_home')
            #return HttpResponse("<h1>Admin Login</h1")

        elif utype == "officer":
            qs = Officer.objects.filter(username_id=un)
            request.session["off_dept"]=qs[0].deparment_id
            request.session["off_un"] = un
            return redirect('officer_home')
            #return HttpResponse("<h1>Officer Login")
        else:
            qs = CitizenRegister.objects.filter(username_id=un)
            if qs[0].status == 'active':
                request.session['ctid'] = qs[0].ctid
                request.session['username'] = un
                return redirect('citizen_home')
            else:
                messages.error(request, "Please Validate Your OTP")
                return redirect('citizen_index')
    else:
        if utype == "admin":
            messages.error(request,"Invalid Admin")
            return redirect('admin_index')
        elif utype == "officer":
            messages.error(request, "Invalid Officer")
            return redirect('officer_index')
        else:
            messages.error(request, "Invalid Citizen")
            return redirect('citizen_index')
