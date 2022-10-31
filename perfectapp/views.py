from http.client import HTTPResponse
import json
from smtplib import SMTPResponseException
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

from perfectapp.models import Question, Score, Userdata, dinalsubmit
def name(request):
    pass
def homepage(request):
    return render(request,'login.html')
def showregister(request):
    return render(request,'register.html')

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        email=request.POST['email']
        mobno=request.POST['mobno']
        photo=request.FILES['photo']
        file=request.FILES['file']

        if password==password1:
            Userdata.objects.create(username=username,password=password,password1=password1,email=email,mobno=mobno,photo=photo,file=file)
            return render(request,'login.html',{'msg':"registation successful"})
        else:
            return render(request,"register.html",{'msg':"password do not match"})

def login(request):
    username=request.GET['username']
    password=request.GET['password']
    if username=='admin' and password=='admin123':
        return render(request,'questionmanagement.html',{'msg':"welcome Admin"})

    try:
        a=Userdata.objects.get(username=username)
        b=Score.objects.get(username=username)
    #print(b)
    #print(type(b))
        if (username==a.username and password==a.password) and username==b.username:
            
            return render(request,'login.html',{"msg":"already submitted "})

           

        
    except Score.DoesNotExist:
        b=None
        if (username==a.username and password==a.password):
            request.session['username']=username
            request.session['ans']={}
            request.session['qno']=0
            request.session['score']=0
            request.session['duration']=180
            request.session['mail']=a.email
            d=Question.objects.all()
            b=d[request.session['qno']]
            return render(request,'welcome.html',{'name':request.session['username'],'h':request.session['mail'],'o':a.photo.url,'subject':b.subject,'qno':b.qno,'question':b.question,'answer':b.answer,'a':b.a,'b':b.b,'c':b.c,'d':b.d})
        else:
            return render(request,'login.html',{"msg":"incorrect username and password "})
       
def add(request):
    subject=request.GET['subject']
    qno=request.GET['qno']
    question=request.GET['question']
    answer=request.GET['answer']
    a=request.GET['A']
    b=request.GET['B']
    c=request.GET['C']
    d=request.GET['D']

    Question.objects.create(subject=subject,qno=qno,question=question,answer=answer,a=a,b=b,c=c,d=d)
    return render(request,"questionmanagement.html",{'ms':"Question added successfully"})

def view(request):
    try:
        qno=request.GET['qno']
        view=Question.objects.get(qno=qno)
        return render(request,"questionmanagement.html",{"e":view,"ms":"question view"})
    except:
        return render(request,"questionmanagement.html",{"ms":"question no not available"})

def update(request):
    qno=request.GET['qno']
    view=Question.objects.filter(qno=qno)
    view.update(
        subject=request.GET['subject'],
    qno=request.GET['qno'],
    question=request.GET['question'],
    answer=request.GET['answer'],
    a=request.GET['A'],
    b=request.GET['B'],
    c=request.GET['C'],
    d=request.GET['D'],
    )
    return render(request,'questionmanagement.html',{'ms':"data updated successfully"})

def delete(request):
    qno=request.GET['qno']
    Question.objects.filter(qno=qno).delete()
    return render(request,"questionmanagement.html",{'ms':"Data deleted of question ="+ qno})

def check(request):
    print(request.GET['username'])
    message="Username Already Present"
    try:
        Userdata.objects.get(username=request.GET['username'])
    except:
        message=""

    data={'msg':message}
    json_data=json.dumps(data)
    response=HttpResponse(f'{json_data}',content_type="application/json")
    return response

def mailcheck(request):

    print(request.GET['mail'])
    msg="Mail id alredy used.used another mail id"
    try:
        Userdata.objects.get(email=request.GET['mail'])
    except:
        msg=""
    data={'msg':msg}      
    json_data=json.dumps(data)
    response=HttpResponse(f'{json_data}',content_type="application/json")
    return response

def next(request):
    try:
        a=Question.objects.all()

        request.session['qno']=request.session['qno']+1
        b=a[request.session['qno']]
        e=b.qno
        all=request.session['ans']
        result=""
        for i,j in all.items():
            if int(i)==e:
                result=j[4]
        return render(request,'welcome.html',{"e":result, 'name':request.session['username'],'h':request.session['mail'],'subject':b.subject,'qno':b.qno,'question':b.question,'answer':b.answer,'a':b.a,'b':b.b,'c':b.c,'d':b.d})
    except:
        request.session['qno']=0
        b=a[request.session['qno']]
        e=b.qno
        all=request.session['ans']
        result=""
        for i,j in all.items():
            if int(i)==e:
                result=j[4]
        return render(request,'welcome.html',{"e":result,'name':request.session['username'],'h':request.session['mail'],'subject':b.subject,'qno':b.qno,'question':b.question,'answer':b.answer,'a':b.a,'b':b.b,'c':b.c,'d':b.d})
def previous(request):

    try:
        a=Question.objects.all()

        request.session['qno']=request.session['qno']-1
        b=a[request.session['qno']]
        e=b.qno
        all=request.session['ans']
        result=""
        for i,j in all.items():
            if int(i)==e:
                result=j[4]

        return render(request,'welcome.html',{"e":result,'name':request.session['username'],'h':request.session['mail'],'subject':b.subject,'qno':b.qno,'question':b.question,'answer':b.answer,'a':b.a,'b':b.b,'c':b.c,'d':b.d})
    except:
        request.session['qno']=1
        b=a[request.session['qno']]
        e=b.qno
        all=request.session['ans']
        result=""
        for i,j in all.items():
            if int(i)==e:
                result=j[4]
        return render(request,'welcome.html',{"e":result,'name':request.session['username'],'h':request.session['mail'],'subject':b.subject,'qno':b.qno,'question':b.question,'answer':b.answer,'a':b.a,'b':b.b,'c':b.c,'d':b.d})

def currentans(request):
    data=request.session['ans']
    data[request.GET['qno']]=list([request.GET['qno'],request.GET['subject'],request.GET['answer'],request.GET['question'],request.GET['op']])
    request.session['ans']=data
    print(request.session['ans'])
    
        
    return render(request,'welcome.html')
def cal(request):
    try:
        print(request.session['ans'])
        list1=request.session['ans']
        listdata=list1.values()
        print(listdata)

        for i in listdata:
            
            if i[2]==i[4]:
                request.session['score']=request.session['score']+1
        finalscore=request.session['score']
        Score.objects.create(username=request.session['username'],score=finalscore)


        d=list(listdata)
        for j in d:
        
            dinalsubmit.objects.create(username=request.session['username'],qno=j[0],subject=j[1],question=j[3],answer=j[2],op=j[4])   
        
        del request.session['username']
        del request.session['score']
        print(finalscore)
        
    except:
        return render(request,"login.html")

    return render(request,"score.html",{"score":finalscore,"listdata":listdata})

def showtime(request):
    request.session['duration']=request.session['duration']-1
    return HttpResponse(request.session['duration'])

