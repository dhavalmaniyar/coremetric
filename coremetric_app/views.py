# from django.core.checks import messages
from django.shortcuts import render
from .models import Comment
# Create your views here.
def index(request):
    return render(request,'index.html')
    
def submit(request):
    rname=request.POST['name']
    rcomment=request.POST['comment']
    remail=request.POST['email']
    submitData=Comment(name=rname,comment=rcomment,email=remail)
    submitData.save()
    return render(request,'index.html',{'message':'Form submitted successfully'})
   