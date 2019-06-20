from django.shortcuts import render,redirect
from ac_login.models import Login
from .models import CitizenRegister,OTP,Complaint
from django.contrib import messages

def citizen_save(request):
    if request.method == "POST":
        name = request.POST.get("name")
        cno = request.POST.get("contact")
        city = request.POST.get("city")
        image = request.FILES["image"]
        address = request.POST.get("address")
        username = request.POST.get("username")
        password = request.POST.get("password")

        one = name[0]
        two = int(cno[0])+int(cno[-1])
        three = username[-3]
        four = password[3]

        otp = four+one+str(two)+three

        mess = sendACASMS(cno,otp)

        import json
        d = json.loads(mess)
        if d["return"]:
            OTP(contact=cno, otp=otp).save()
            Login(username=username,password=password,usertype='citizen').save()
            CitizenRegister(name=name,contact=cno,image=image,city=city,address=address,username_id=username,status='pending').save()
            #return render(request,"ac_citizen/citizen_index.html",{"message":"Registered"})
            return render(request,"ac_citizen/citizen_otpcheck.html",{"message":"OTP is Pending"})
        else:
            return render(request, "ac_citizen/citizen_register.html", {"message": "Wrong Contact No"})


def sendACASMS(contactno,otp):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=Your One Time Password to Register : "+otp+"&language=english&route=p&numbers="+contactno
    headers = {
        'authorization': "OmgfGSeqd49CbLrTwUAN0MPJxyt3ZE1l7FV2RDcv58uKjhaXnBymtEP9Agv2q3VscNwIDiQaronejlZM",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.text


def citizen_otp_check(request):
    if request.method == "POST":
        otp = request.POST.get("otp")
        cno = request.POST.get("cno")
        qs = OTP.objects.filter(contact=cno,otp=otp)
        if qs:
            CitizenRegister.objects.filter(contact=cno).update(status='active')
            messages.error(request,"OTP is Valid")
            return redirect('citizen_index')
        else:
            messages.error(request,"Invalid OTP")
            return redirect('citizen_otp_check')


def citizenLogout(request):
    del request.session['username']
    return redirect('main_page')


def complaintRegister(request):
    if request.method == "POST":
        cid = request.POST.get("cid")
        ctid = request.POST.get("ctid")
        dept = request.POST.get("dept")
        message = request.POST.get("message")
        image = request.FILES["image"]
        status = "pending"
        Complaint(cid=cid,ctid_id=ctid,department_id=dept,message=message,image=image,status=status).save()
        messages.error(request,"Complaint Registered")
        return redirect('citizen_home')


def citizen_close_complaint(request):
    cid = request.session['ctid']
    qs = Complaint.objects.filter(ctid_id=cid,status='closed')
    return render(request,"ac_citizen/citizen_closed_complaints.html",{"object_list":qs})