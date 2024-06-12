from django.db import models
# Create your models here.

# class UserCredential(models.Model):
#     Email=models.CharField(max_length=100)
#     Pswd=models.CharField(max_length=50)
#     Fname=models.CharField(max_length=50)
#     Lname=models.CharField(max_length=50)
#     dob=models.DateField()
#     FtherName=models.CharField(max_length=50)
#     MotherName=models.CharField(max_length=50)
#     CurAddress=models.CharField(max_length=50)
#     PermanentAdd=models.CharField(max_length=50)
#     Adhar=models.IntegerField()
#     Pan=models.CharField(max_length=50)
#     Votter=models.CharField(max_length=50)
#     img=models.ImageField(upload_to='pics')
#     PhoneNum=models.IntegerField()
#     Nationality=models.CharField(max_length=50)
#     gender=models.CharField(max_length=50)
#     Father_pof=models.CharField(max_length=50)
#     Mother_pof=models.CharField(max_length=50)
#     cast=models.CharField(max_length=50)

# class Academics(models.Model):
#     SecondaryEdu=models.CharField(max_length=100)
#     HigherSecondaryEdu=models.TextField()
#     AdditionalActivity=models.TextField()
#     Projects=models.TextField()
#     Achievements=models.CharField(max_length=100)
#     Awards=models.CharField(max_length=100)

# class UniversityDetails(models.Model):
#     Branch=[
#         ('CSE','CSE'),
#         ('ECE','ECE'),
#         ('ME','ME'),
#         ('CV','CV'),
#         ('BT','BT'),
#         ('EE','EE'),
#     ]
#     PassingYear=models.IntegerField()
#     Hosteler=models.BooleanField()
#     HostelName=models.CharField(max_length=100)
#     Fees=models.IntegerField()
#     ClassTime=models.TimeField()
#     CourseBranch=models.CharField(max_length=10,choices=Branch,default='CSE')
#     ExamScore=models.IntegerField()

# class Attendnce(models.Model):
#     Percentage=models.IntegerField()
#     LeapeReq=models.BooleanField(default=False)
#     HomeAddress=models.CharField(max_length=100)
#     Reason=models.TextField()
#     Proctor=models.CharField(max_length=100)

# class Placement(models.Model):
#     PlacedOrNot=models.BooleanField(default=False)
#     Internship=models.TextField()
#     Training=models.TextField()
#     Resume=models.TextField()
#     Development=models.TextField()


# class TempPersonalDetails(models.Model):
#     id=models.IntegerField(primary_key=True)
#     Name=models.CharField(max_length=100)
#     Email=models.EmailField(max_length=100)
#     HigherEducation=models.CharField(max_length=100)
#     GuardianName=models.CharField(max_length=100)
#     Number=models.IntegerField()
#     Address=models.TextField()
#     Age=models.IntegerField()

# class TempAcademics(models.Model):
#     id=models.IntegerField(primary_key=True)
#     SecondaryEdu=models.CharField(max_length=100)
#     HigherSecondaryEdu=models.TextField()
#     AdditionalActivity=models.TextField()
#     Projects=models.TextField()
#     Achievements=models.CharField(max_length=100)
#     Awards=models.CharField(max_length=100)

# class TempPlacement(models.Model):
#     id=models.IntegerField(primary_key=True)
#     PlacedOrNot=models.BooleanField(default=False)
#     Internship=models.TextField()
#     Training=models.TextField()
#     Resume=models.TextField()
#     Development=models.TextField()

# class Admin(models.Model):
#     universityid=models.CharField(max_length=100)
#     pswd=models.CharField(max_length=100)
#     universityname=models.CharField(max_length=100)

# class Uploader(models.Model):
#     UploaderId=models.CharField(max_length=100)
#     pswd=models.CharField(max_length=100)
    

class University(models.Model):
    Uid=models.IntegerField(primary_key=True)
    UName=models.CharField(max_length=100)
    BName=models.CharField(max_length=100)
    UserMail=models.CharField(max_length=100)
    pswd=models.CharField(max_length=100)

class Admin(models.Model):
    Uid=models.IntegerField(primary_key=True)
    AdminMail=models.CharField(max_length=100)
    pswd=models.CharField(max_length=100)

class UploaderCredential(models.Model):
    U_mail=models.CharField(max_length=100)
    Uid=models.IntegerField(primary_key=True)
    pswd=models.CharField(max_length=100)
    institute_name=models.CharField(max_length=100)
    R1=models.BooleanField(default=False)
    R2=models.BooleanField(default=False)
    tellaboutself=models.TextField()

class UploaderCert(models.Model):
    sid=models.IntegerField(primary_key=True)   
    Uid=models.IntegerField()
    University_name=models.CharField(max_length=100)
    Student_name=models.CharField(max_length=100)
    Course_name=models.CharField(max_length=100)
    Course_credit=models.IntegerField()
    score=models.IntegerField()
    Aicte_app=models.BooleanField(default=False)
    certi=models.CharField(max_length=100)

class Personaldetails(models.Model):
    sid=models.IntegerField(primary_key=True)
    Fname=models.CharField(max_length=100)
    Lname=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    mail_id=models.CharField(max_length=100)
    Father_name=models.CharField(max_length=100)
    Father_prof=models.CharField(max_length=100)
    Mother_name=models.CharField(max_length=100)
    Mother_prof=models.CharField(max_length=100)
    current_add=models.TextField()
    permanent_add=models.TextField()

class TempPersonaldetails(models.Model):
    sid=models.IntegerField(primary_key=True)
    phone_no=models.IntegerField()
    Father_prof=models.CharField(max_length=100)
    Mother_prof=models.CharField(max_length=100)
    current_add=models.TextField()

# class Academics(models.Model):
#     sid=models.IntegerField(primary_key=True)
#     secondary_edu=models.CharField(max_length=100)
#     secondary_inst=models.CharField(max_length=100)
#     higher_edu_per=models.CharField(max_length=100)
#     higher_inst=models.CharField(max_length=100)
#     score_secondary=models.IntegerField()
#     score_higher=models.IntegerField()
#     university_name=models.CharField(max_length=100)
#     score_univ=models.IntegerField()
#     anoth_achiv=models.CharField(max_length=100)
#     cgpa=models.IntegerField()
#     attendance=models.IntegerField()

class Academics(models.Model):
    smail=models.CharField(max_length=100,primary_key=True)
    secondary_institute=models.CharField(max_length=100)
    secondary_score=models.CharField(max_length=100)
    higher_institute=models.CharField(max_length=100)
    higher_score=models.IntegerField()
   

class C_Academics(models.Model):
    university_name=models.CharField(max_length=100)
    b_name=models.CharField(max_length=100)
    sid=models.IntegerField(primary_key=True)
    cgpa=models.IntegerField()
    attendance=models.IntegerField()

class Govt_Doc(models.Model):
    sid=models.IntegerField(primary_key=True)
    Adhar_Num=models.IntegerField()
    Adhar_Doc=models.ImageField(upload_to='Adhar_Doc')
    Pan_Num=models.CharField(max_length=100)
    Pan_Doc=models.ImageField(upload_to='Pan_Doc')
    Votter_num=models.CharField(max_length=100)
    Votter_Doc=models.ImageField(upload_to='Votter_Doc')  #file
    Caste_id=models.CharField(max_length=100)
    Caste_Doc=models.ImageField(upload_to='Caste_Doc')

class TNP(models.Model):
    Uid=models.IntegerField()
    Bid=models.IntegerField()
    sid=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=100)
    course_credit=models.CharField(max_length=100)
    course_score=models.CharField(max_length=100)
    aicte_approv=models.BooleanField(default=False)
    catagory=models.CharField(max_length=100)
    certificate=models.ImageField(upload_to='certificate') #file

class Certificate(models.Model):
    sid=models.IntegerField(primary_key=True)
    Cer1Name=models.CharField(max_length=100)
    Cer1=models.ImageField(upload_to='certificate')
    Cer2Name=models.CharField(max_length=100)
    cer2=models.ImageField(upload_to='certificate')
    Cer3Name=models.CharField(max_length=100)
    cer3=models.ImageField(upload_to='certificate')
    Cer4Name=models.CharField(max_length=100)
    cer4=models.ImageField(upload_to='certificate')
    Cer5Name=models.CharField(max_length=100)
    cer5=models.ImageField(upload_to='certificate')  #file

