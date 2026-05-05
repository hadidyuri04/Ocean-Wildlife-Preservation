from django.shortcuts import render , HttpResponse, redirect

# Create your views here.
def home(request):
    return render(request,'MainPages/LandingPage.html')

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
