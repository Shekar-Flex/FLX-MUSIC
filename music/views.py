from flx_music_player import settings
from django.shortcuts import render
from .models import Song_data
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

# global x,data
# x=0
data=Song_data.objects.all()
# lis=list(Song_data.objects.all())

def home(request):
    return render(request,'home.html')

def play(request):
    data=Song_data.objects.all()
    # lis=list(Song_data.objects.all())
    # lis=[1,2,3,4]
    print(lis)
    # print("song")
    # print(data)
    global x,lens
    lens=len(data)-1
    if request.method=='GET':
        x=0
        send=data[x]
        # print(send)
        return render(request,'play.html',{'obj':send,'leng':lens,'x':x})
    else:
        # print(x)
        if(x!=lens):
            x+=1
        else:
            x=0
        # print(x)
        send=data[x]
        # print(send)
        return render(request,'play.html',{'obj':send,'leng':lens,'x':x})
def playback(request):
    global x,lens
    if request.method=='POST':
        if(x!=0):
            x-=1
        else:
            x=lens
        send=data[x]
        # print(send)
        return render(request,'play.html',{'obj':send,'leng':lens,'x':x})
    else:
        return render(request,'home.html')

def report(request):
    if request.method=='GET':
        return render(request,'rep.html')
    elif request.method=='POST':
        sub=request.POST['title']
        mess=request.POST['mess']
        from_email=settings.EMAIL_HOST_USER
        smail='shekardharmalingam1234@gamil.com'
        to_email=[smail]
        # print(sub,mess,from_email,to_email)
        send_mail(sub,mess,from_email,to_email,fail_silently=True)
        messages.success(request,'Your Request send Sucessfully!...')
        return render(request,'rep.html')
    else:
        return render(request,'home.html')