
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import profiles
# from django.contrib.auth.models import profiles
# Create your views here.
def home(request):
    return render (request, 'home.html') 

def login(request):
    return render(request, 'login.html')

def addNew(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print(request.POST)
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        callNumber = request.POST.get('mobileNum')
        whatsappNumber = request.POST.get('Whatsapp') 
        ministry = request.POST.get('ministry')
        centre =request.POST.get('center')
        campus = request.POST.get('campus/workPlace') 
        hostel_address  = request.POST.get('hostel/homeAddress') 
        city = request.POST.get('city') 
        qualification = request.POST.get('qualification')
        profession = request.POST.get('profession') 
        maritalStatus = request.POST.get('optional2')
        bacenta = request.POST.get('bacenta') 
        layschool = request.POST.get('layschool') 
        imagefile = request.FILES['images'] 
        
        member = profiles(firstname = firstname,
                          lastname = lastname, 
                          gender = gender,
                          dob = dob,
                          callNumber = callNumber,
                          whatsappNumber = whatsappNumber,
                          ministry = ministry,
                          centre = centre,
                          campus = campus,
                          hostel_address = hostel_address,
                          city = city,
                          qualification = qualification,
                          profession = profession,
                          maritalStatus = maritalStatus,
                          bacenta = bacenta,
                          layschool = layschool,
                          imagefile = imagefile
        )
        member.save()
        return redirect('/members')
    else:
       return render(request, 'newRegistration.html')   

  

def members(request):
    all_members = profiles.objects.all()
    return render(request, 'membersInfo.html',
    {'all_items': all_members })


def delete(request, member_id):
    # if request.method == 'POST':
    member_to_delete = profiles.objects.get(id = member_id)
    print(member_to_delete)
    print("rdtfyguhkljk")
    member_to_delete.delete()
        # return redirect('/login')
    # else:
    return redirect('/members')
   
