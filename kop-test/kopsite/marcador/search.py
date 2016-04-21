from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
# from itertools import *
from django.db import connection
from marcador.forms import UserForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


# Create your views here.
def dictfetchall(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

def run_search(request):
  # if request.GET:
  if request.POST:
    form = UserForm(request.POST)

    if form.is_valid():
      user_name = form.cleaned_data['user_name']

      query_string = "select b.title,b.url from auth_user a, marcador_bookmark b where a.id=b.owner_id and a.username='%s'" % user_name
      cursor = connection.cursor()
      cursor.execute(query_string)

      rows = dictfetchall(cursor)
      return render(request, 'marcador/query_results.html',{'bookmarks': rows})
  else:
    form = UserForm()

    #return render_to_response('marcader.user.html', args)
    return render(request,'marcador/user.html', {'form':form})
