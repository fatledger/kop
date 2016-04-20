from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^dataanalysis', views.analysis, name='dataanalysis'),
    url(r'^dataintegrate', views.integrate, name='dataintegrate'),
    url(r'^datashare', views.addContactInfo, name='datashare'),
    url(r'^about_us', views.aboutus, name='about_us'),
    url(r'^login', views.loginview, name='login'),    
    url(r'^logout', views.logoutview, name='logout'),
    url(r'^create_user', views.getUserInput, name='create_user'),
	url(r'^myaccount', views.getUserProfile, name='myaccount'),
	url(r'^mydata', views.mydata, name='mydata'),	
    url(r'^(?P<mydata_id>[0-9]+)/mydetail', views.mydetail, name='mydetail'),
    url(r'^adddata', views.addmydata, name='adddata'),
    url(r'^(?P<mydata_id>[0-9]+)/editdata', views.editmydata, name='editdata'),
    url(r'^(?P<mydata_id>[0-9]+)/uploadfile', views.upload_file, name='uploadfile'),
    url(r'^thanks', views.thanks, name='thanks'),
    url(r'^edit_user', views.editUserProfile, name='edit_user'),
    url(r'^pwpwpw', views.changePassword, name='change_password'),
    url(r'^(?P<mydata_id>[0-9]+)/analysis', views.addmyquery, name='analysis'),
]