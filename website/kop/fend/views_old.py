from django.http import Http404
from django.shortcuts import render
from .models import Mydata
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import UserForm
from .forms import DataForm
from django.contrib.auth import views as auth_views

# Create your views here.
def index(request):    
    return render(request, 'kopdata/index.html')

def analysis(request):
    return render(request, 'kopdata/dataanalysis.html')

def integrate(request):
    return render(request, 'kopdata/dataintegrate.html')

def share(request):
    return render(request, 'kopdata/datashare.html')

def aboutus(request):
    return render(request, 'kopdata/about_us.html')

def loginview(request):
    template_response = auth_views.login(request, 'kopdata/login.html')
    return template_response
    
def logoutview(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'kopdata/index.html')

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
                        return render(request, 'kopdata/index.html')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()
    return render(request, 'kopdata/create_user.html', {'form': form})
    
def mydata(request):
    try:
        data_list = Mydata.objects.get(my_user_name=request.user.username)
    except Mydata.DoesNotExist:
        return render(request, 'kopdata/mydata.html')
    context = {'user_data_list': data_list}
    return render(request, 'kopdata/mydata.html', context)

def mydetail(request, mydata_id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if not mydata_id:
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
             else:
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
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()
        form.fields["my_field"]   
    return render(request, 'kopdata/mydetail.html', {'form': form})