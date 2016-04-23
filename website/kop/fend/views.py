from django.http import Http404
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.utils import timezone
from .models import Mydata, UserProfile, ContactInfo, MyDataQuery
from .forms import UserForm, UserProfileForm
from .forms import DataForm, ChangePWForm
from .forms import UploadFileForm, RequestForm

# Create your views here.
def index(request):    
    return render(request, 'fend/index.html')

def analysis(request):
    return render(request, 'fend/dataanalysis.html')

def integrate(request):
    return render(request, 'fend/dataintegrate.html')

def share(request):
    return render(request, 'fend/datashare.html')

def aboutus(request):
    return render(request, 'fend/about_us.html')

def thanks(request):
    return render(request, 'fend/thanks.html')

def loginview(request):
    template_response = auth_views.login(request, 'fend/login.html')
    return template_response
    
def logoutview(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'fend/index.html')

def getUserInput(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            pw1 = form.cleaned_data.get("password1")
            pw2 = form.cleaned_data.get("password2")
            if pw1 and pw2 and pw1 == pw2:
                un = form.cleaned_data.get("user_name")
                em = form.cleaned_data.get("email")
                user = User.objects.create_user(username=un, email=em, password=pw1)
                user.last_name = form.cleaned_data.get("last_name")
                user.first_name = form.cleaned_data.get("first_name")
                user.save()
                user = authenticate(username=un, password=pw1)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        userprofile = UserProfile(my_user_name=request.user.username, create_date=timezone.now())
                        userprofile.phone = form.cleaned_data.get("phone")
                        userprofile.title = form.cleaned_data.get("title")
                        userprofile.company = form.cleaned_data.get("company")
                        userprofile.address = form.cleaned_data.get("address")
                        userprofile.city = form.cleaned_data.get("city")
                        userprofile.state = form.cleaned_data.get("state")
                        userprofile.country = form.cleaned_data.get("country")
                        userprofile.save()
                        return render(request, 'fend/mydata.html')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()
    return render(request, 'fend/create_user.html', {'form': form})

def getUserProfile(request):
    try:
        data = UserProfile.objects.get(my_user_name=request.user.username)
    except Mydata.DoesNotExist:
        return render(request, 'fend/myaccount.html')
    context = {'user_data': data}
    return render(request, 'fend/myaccount.html', context)
 
def editUserProfile(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():            
            userprofile = UserProfile.objects.get(my_user_name=request.user.username)
            userprofile.phone = form.cleaned_data.get("phone")
            userprofile.title = form.cleaned_data.get("title")
            userprofile.company = form.cleaned_data.get("company")
            userprofile.address = form.cleaned_data.get("address")
            userprofile.city = form.cleaned_data.get("city")
            userprofile.state = form.cleaned_data.get("state")
            userprofile.country = form.cleaned_data.get("country")
            userprofile.save()
            context = {'user_data': userprofile}
            return render(request, 'fend/myaccount.html', context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserProfileForm()
        data = UserProfile.objects.get(my_user_name=request.user.username)
        datalist = {'phone' : data.phone, 'title' : data.title, 'company' : data.company,
        'address' : data.address, 'city' : data.city, 'state' : data.state,
        'country' : data.country}
        form = UserProfileForm(datalist, initial=datalist)
    return render(request, 'fend/edit_user.html', {'form': form})

def changePassword(request):
    if request.method == 'POST':
        form = ChangePWForm(request.POST)
        if form.is_valid():
            newpassword=form.cleaned_data['newpassword1']
            username=request.user.username
            password=form.cleaned_data['oldpassword']
            user = authenticate(username=username, password=password)
            if user is not None:
                user.set_password(newpassword)
                user.save()
                userprofile = UserProfile.objects.get(my_user_name=request.user.username)            
                context = {'user_data': userprofile}
                return render(request, 'fend/myaccount.html', context)
            else:
                return render(request, 'fend/pwpwpw.html',{'error':'You have entered wrong old password','form': form})
        else:
           return render(request, 'fend/pwpwpw.html',{'error':'You have entered old password','form': form})
    else:
        form = ChangePWForm()
    return render(request, 'fend/pwpwpw.html', {'form': form})
     
def mydata(request):
    try:
        data_list = Mydata.objects.filter(my_user_name=request.user.username)
    except Mydata.DoesNotExist:
        return render(request, 'fend/mydata.html')
    context = {'user_data_list': data_list}
    return render(request, 'fend/mydata.html', context)

def mydetail(request, mydata_id):
    try:
        detaildata = Mydata.objects.get(id=mydata_id)
    except Mydata.DoesNotExist:
        return render(request, 'fend/mydata.html')
    context = {'detail_data': detaildata}
    return render(request, 'fend/mydetail.html', context)

def addmydata(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DataForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = Mydata(my_user_name=request.user.username, create_date=timezone.now())
            data.data_name = form.cleaned_data.get("data_name")
            data.smoke_status = form.cleaned_data.get("smoke_status")
            data.gender = form.cleaned_data.get("gender")
            data.sick_type = form.cleaned_data.get("sick_type")
            data.life_status = form.cleaned_data.get("life_status")
            data.ICDO3 = form.cleaned_data.get("ICDO3")
            data.patho_status = form.cleaned_data.get("patho_status")
            data.data_des = form.cleaned_data.get("data_des")            
            data.save()
            data_list = Mydata.objects.filter(my_user_name=request.user.username)
            context = {'user_data_list': data_list}
            return render(request, 'fend/mydata.html', context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = DataForm()
    return render(request, 'fend/adddata.html', {'form': form})

def editmydata(request, mydata_id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DataForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = Mydata.objects.get(id=mydata_id)
            data.data_name = form.cleaned_data.get("data_name")
            data.smoke_status = form.cleaned_data.get("smoke_status")
            data.gender = form.cleaned_data.get("gender")
            data.sick_type = form.cleaned_data.get("sick_type")
            data.life_status = form.cleaned_data.get("life_status")
            data.ICDO3 = form.cleaned_data.get("ICDO3")
            data.patho_status = form.cleaned_data.get("patho_status")
            data.data_des = form.cleaned_data.get("data_des")            
            data.save()
            context = {'detail_data': data}
            return render(request, 'fend/mydetail.html', context)
    # if a GET (or any other method) we'll create a blank form
    else:        		
        data = Mydata.objects.get(id=mydata_id)
        datalist = {'data_name' : data.data_name, 'smoke_status' : data.smoke_status, 'gender' : data.gender,
		'sick_type' : data.sick_type, 'life_status' : data.life_status, 'ICDO3' : data.ICDO3,
        'patho_status' : data.patho_status, 'data_des' : data.data_des}
        form = DataForm(datalist, initial=datalist)
    return render(request, 'fend/editdata.html', {'form': form})

def upload_file(request, mydata_id):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data = Mydata.objects.get(id=mydata_id)
            data.genome_file = request.FILES['genome_file']
            data.save()
            context = {'detail_data': data}
            return render(request, 'fend/mydetail.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'fend/uploadfile.html', {'form': form})

def addContactInfo(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RequestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = ContactInfo()
            data.name = form.cleaned_data.get("name")
            data.created_date=timezone.now()
            data.email = form.cleaned_data.get("email")
            data.tittle = form.cleaned_data.get("tittle")
            data.company = form.cleaned_data.get("company")
            data.address = form.cleaned_data.get("address")
            data.city = form.cleaned_data.get("city")
            data.state = form.cleaned_data.get("state")
            data.country = form.cleaned_data.get("country")
            data.phone = form.cleaned_data.get("phone")
            data.description = form.cleaned_data.get("description")
            data.save()            
            context = {'name': data.name}
            return render(request, 'fend/thanks.html', context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RequestForm()        
    return render(request, 'fend/datashare.html', {'form': form})

def addmyquery(request, mydata_id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DataForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            query = MyDataQuery(my_user_name=request.user.username, create_date=timezone.now())
            query.mydata_id = mydata_id
            query.data_name = form.cleaned_data.get("data_name")
            query.smoke_status = form.cleaned_data.get("smoke_status")
            query.gender = form.cleaned_data.get("gender")
            query.sick_type = form.cleaned_data.get("sick_type")
            query.life_status = form.cleaned_data.get("life_status")
            query.ICDO3 = form.cleaned_data.get("ICDO3")
            query.patho_status = form.cleaned_data.get("patho_status")
            data = Mydata.objects.get(id=mydata_id)
            query.genome_file = data.genome_file
            query.save()
            #add run query function here, the results may also write into a "result" table, and then			
            #pass the record for the results to a 'fend/results.html'. 
            #use query.genome_file.content.path for the file name
			#or MEDIA_ROOT + query.genome_file
            context = {'detail_data': data}
            return render(request, 'fend/mydetail.html', context)            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = DataForm()
        data = Mydata.objects.get(id=mydata_id)
        datalist = {'data_name' : data.data_name, 'smoke_status' : data.smoke_status, 'gender' : data.gender,
		'sick_type' : data.sick_type, 'life_status' : data.life_status, 'ICDO3' : data.ICDO3,
        'patho_status' : data.patho_status, 'data_des' : data.data_des}
        form = DataForm(datalist, initial=datalist)
    return render(request, 'fend/analysis.html', {'form': form})
