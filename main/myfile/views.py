from django.shortcuts import render, HttpResponse

from . models import myuploadfile

import subprocess

# Create your views here.
def index(request):
    return render(request,"index.html")

def send_files(request):
    if request.method == "POST":
        name = request.POST.get("filename")
        myfile = request.FILES.getlist("uploadfoles")
        for f in myfile:
            myuploadfile(f_name=name, myfiles=f).save()




        subprocess.call(['python', r'/home/redal/Desktop/scan/scan/main/media/nmap.py'])


        return HttpResponse("ok")







