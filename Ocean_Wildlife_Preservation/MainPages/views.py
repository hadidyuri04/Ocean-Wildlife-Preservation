from django.shortcuts import render , HttpResponse, redirect
from django.conf import settings
import os
import csv
# Create your views here.
def home(request):
    impact_items=[]
    file_path = os.path.join(settings.BASE_DIR, 'MainPages', 'static', 'MainPages', 'css', 'data', 'impact.csv')
    if os.path.exists(file_path):
        with open(file_path, mode='r',encoding='utf-8') as file:
            reader=csv.DictReader(file)
            for row in reader:
                impact_items.append(row)
    print(f"Items found: {len(impact_items)}")
    
    return render(request, 'MainPages/LandingPage.html',{'impact_items' : impact_items} )
def blogs(request):
    return render(request,'MainPages/blogs.html')
def PrivatePolicy(request):
    return render(request,'MainPages/PrivatePolicy.html')
def GetInformation(request):
    if request.method =='POST':
        print(" hello")
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        with open(r"C:\Users\Administrator\Desktop\informationTxt.txt","a") as file:
            file.write(f"{name},{email},{message}\n")
        return redirect("home")
    return render(request,'MainPages/LandingPage.html')
def AdminPageInfo(request):
    Student=[]
    with open(r"C:\Users\Administrator\Desktop\informationTxt.txt","r") as file:
        for line in file:
            line=line.strip()
            if line:
                name,email,message=line.split(",")
                Student.append({"name":name,"email":email,"message":message})
    return render(request,"MainPages/AdminPage.html",{"student":Student})
def PrintPrivatePolicy(request):
    file_path = os.path.join(settings.BASE_DIR, 'MainPages', 'static', 'MainPages', 'css', 'data', 'PrivatePolicyDoc.txt')
    with open(file_path,'r') as file:
         file_content=file.read()
    return render(request,'MainPages/PrivatePolicy.html',{'content': file_content})
def Blog1Page(request):
    return render(request, 'MainPages/Blog1Page.html')
def Blog2Page(request):
    return render(request, 'MainPages/Blog2Page.html')
def Blog3Page(request):
    return render(request, 'MainPages/Blog3Page.html')
              