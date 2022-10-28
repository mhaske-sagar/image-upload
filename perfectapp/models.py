from distutils.command.upload import upload
from django.db import models

class Userdata(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    password1=models.CharField(max_length=20)
    email=models.EmailField()
    mobno=models.CharField(max_length=10)
    photo=models.ImageField(upload_to="photo/")
    file=models.FileField(upload_to="file/")

    def __str__(self):
        return ("{},{},{},{},{},{},{}".format(self.username,self.password,self.password1,self.email,self.mobno,self.photo,self.file))

class Question(models.Model):
    qno=models.IntegerField(primary_key=True)
    subject=models.CharField(max_length=20)
    question=models.CharField(max_length=100)
    answer=models.CharField(max_length=40)
    a=models.CharField(max_length=20)
    b=models.CharField(max_length=20)
    c=models.CharField(max_length=20)
    d=models.CharField(max_length=20)

    def __str__(self):
        return ("{},{},{},{},{},{},{},{}".format(self.qno,self.subject,self.question,self.answer,self.a,self.b,self.c,self.d))

class dinalsubmit(models.Model):
    username=models.CharField(max_length=20)
    qno=models.IntegerField(primary_key=True)
    subject=models.CharField(max_length=20)
    question=models.CharField(max_length=100)
    answer=models.CharField(max_length=40)
    op=models.CharField(max_length=10)

    def __str__(self):
        return ("{},{},{},{},{},{}".format(self.username,self.qno,self.subject,self.question,self.answer,self.op))

    class Meta:
        db_table='finaldata'    

class Score(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    score=models.IntegerField()

    def __str__(self):
        return("{},{}".format(self.username,self.score))

    class Meta:
        db_table='score'


        
