from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('paasswordcheck',views.paasswordcheck,name='paasswordcheck'),
    path('LogOut',views.LogOut,name='LogOut'),
    path('RegisterUser',views.RegisterUser,name='RegisterUser'),
    path('ForgetPassword',views.ForgetPassword,name='ForgetPassword'),
    path('SendOtp',views.SendOtp,name='SendOtp'),
    path('verify_otp',views.verify_otp,name='verify_otp'),
    path('ChangePass',views.ChangePass,name='ChangePass'),
    path('AdminLogin',views.AdminLogin,name='AdminLogin'),
    path('UploaderLogin',views.UploaderLogin,name='UploaderLogin'),
    path('verify_otp_fg_stu',views.verify_otp_fg_stu,name='verify_otp_fg_stu'),
    path('RegisterOtpSend',views.RegisterOtpSend,name='RegisterOtpSend'),
    path('RegisterOtpVerify',views.RegisterOtpVerify,name='RegisterOtpVerify'),
    path('LoginAsCompany',views.LoginAsCompany,name='LoginAsCompany'),
    path('UploaderRegister',views.UploaderRegister,name='UploaderRegister'),
    path('SaveUploader',views.SaveUploader,name='SaveUploader'),
    
]