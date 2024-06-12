from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.views.decorators.cache import cache_control
import smtplib
import ssl
import random
from django.core.files.storage import FileSystemStorage

# Create your views here.

def login(request):
    return render(request,'loginform.html')
uname=""
skey=""
lgvalue=False
OTP=''

def otpgenerator():
    global OTP
    int1 =str(random.randint(0, 9))
    int2 =str(random.randint(0, 9))
    int3 =str(random.randint(0, 9))
    int4 =str(random.randint(0, 9))

    final=int1+int2+int3+int4
    print(OTP)
    OTP=int(final)
    return final

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def paasswordcheck(request):
    global uname,skey
    if request.method=='POST':
        uname=request.POST['uname']
        pswd=request.POST['pswd']
        if University.objects.filter(UserMail=uname,pswd=pswd).exists():
            skey=University.objects.filter(UserMail=uname,pswd=pswd).values_list('Uid')[0][0]
            print(skey)
            mailsender(uname,otpgenerator())
            return render(request,'verify_otp.html',{'Alert':False})
        else:
            return render(request,'loginform.html',{'Alert':True})
    else:
        return render(request,'loginform.html')
    
def StudentDataFetcher():
    PDetails=Personaldetails.objects.get(sid=skey)
    AcademicsDetails=Academics.objects.get(smail=PDetails.mail_id)
    AcademicsDetails2=C_Academics.objects.get(sid=skey)
    Govt_DocDetails=Govt_Doc.objects.get(sid=skey)
    TNPDetails=TNP.objects.get(sid=skey)
    

    return [PDetails,AcademicsDetails,AcademicsDetails2,Govt_DocDetails,TNPDetails]

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def verify_otp(request):
    webotp=request.POST['otp']
    global OTP
    if OTP==int(webotp):
        data=StudentDataFetcher()
        return render(request,'index.html',{'datas':data})
    else:
        return render(request,'verify_otp.html',{'Alert':True})

def mailsender(uname,msg):
    # pass
    smtp_port = 587          
    smtp_server = "smtp.gmail.com" #Google SMTP Server
    email_from='mail@gamil.com'
    email_to=uname
    pswd=""
    # content of message
    message=msg
    simple_email_context = ssl.create_default_context()
    try:
        print("Connecting to server.....")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls(context=simple_email_context)
        TIE_server.login(email_from,pswd)
        print("connected to server :-)")
        print("Connecting to server.....")
        print(f"sending email to -{email_to}")
        TIE_server.sendmail(email_from, email_to , message)
        print(f"Email succesfully sent to - {email_to}")
    except Exception as e:
        print(e)
    finally:
        TIE_server.quit()    


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def LogOut(request):
    lgvalue=False
    return render(request,'loginform.html')

def RegisterUser(request):
    return render(request,'registeruser.html')

def ForgetPassword(request):
    return render(request,'forget.html')


mail=''
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def SendOtp(request):
    global mail
    mail=request.POST['email']
    mailsender(mail,otpgenerator())
    return render(request,'verify_otp_fg_stu.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def ChangePass(request):
    global mail
    p1=University.objects.get(UserMail=mail)
    if request.POST['pass']==request.POST['cpass']:
        p1.pswd=request.POST['pass']
        p1.save()
        return render(request,'loginform.html')
    else:
        return render(request,'setpass.html')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def verify_otp_fg_stu(request):
    webotp=request.POST['otp']
    global OTP
    if OTP==int(webotp):
        return render(request,'setpass.html')
    else:
        return render(request,'verify_otp_fg_stu.html',{'Alert':True})
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def AdminLogin(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pswd=request.POST['pass']
        if Admin.objects.filter(Uid=uname,pswd=pswd).exists():
            c1=list(UploaderCredential.objects.all())
            print(c1)
            return render(request,'admin.html',{'Alert':False,'looper':c1})
        else:
            return render(request,'loginform.html',{'Alert':True})
    else:
        return render(request,'loginform.html')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def UploaderLogin(request):
    if request.method=='POST':
        uname=request.POST['uploaderId']
        pswd=request.POST['pass']
        if UploaderCredential.objects.filter(Uid=uname,pswd=pswd).exists():
            return render(request,'uploader.html',{'Alert':False})
        else:
            return render(request,'loginform.html',{'Alert':True})
    else:
        return render(request,'loginform.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def RegisterOtpSend(request):
    global mail
    mail=request.POST['email']
    mailsender(mail,otpgenerator())
    return render(request,'registeruser.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def RegisterOtpVerify(request):
    webotp=request.POST['otp']
    global OTP
    if OTP==int(webotp):
        PDetails=University.objects.filter(UserMail=mail).values()
        msg=str("Thank you for registering....Your user id is "+str(PDetails[0]["Uid"])+" Password is "+str(PDetails[0]["pswd"]))
        print(msg)
        mailsender(mail,msg)
        return render(request,'loginform.html')
    else:
        return render(request,'registeruser.html',{'Alert':True})
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def LoginAsCompany(request):
    return render(request,'company.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def UploaderRegister(request):
    return render(request,'UploaderRegis.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def SaveUploader(request):
    c1=UploaderCredential(U_mail=request.POST['email'],Uid=otpgenerator(),pswd=otpgenerator(),institute_name=request.POST['institute'],tellaboutself=request.POST['tellaboutself'])
    c1.save()
    mailsender(request.POST['email'],"We will contact you after verification. Thank You For Registering")
    return render(request,'loginform.html')

