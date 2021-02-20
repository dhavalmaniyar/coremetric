# from django.core.checks import messages
from django.shortcuts import render
from .models import Comment,User,UserCount
from django.db.models import Q
# Create your views here.
def index(request):
    def get_ip(request):
        address=request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip=address.split(',')[-1].strip()
        else:
            ip=request.META.get('REMOTE_ADDR')
        return ip
    ip=get_ip(request)
    u=User(user=ip)
    result=User.objects.filter(Q(user__icontains=ip))
    print("EEEEEEEEEEEERRRR",result)
    if len(result)==1:
        print("user exist")
    elif len(result)>1:
        print("user exist more...")
    else:
        u.save()
        print("user is unique")
    count=User.objects.all().count()

    datacount=UserCount.objects.get(id=1)
    datacount.ucount=count
    datacount.save()  
    print("count ????????",count)
    return render(request,'index.html')
    
def submit(request):
    rname=request.POST['name']
    rcomment=request.POST['comment']
    remail=request.POST['email']
    submitData=Comment(name=rname,comment=rcomment,email=remail)
    submitData.save()
    return render(request,'index.html',{'message':'Form submitted successfully'})
   