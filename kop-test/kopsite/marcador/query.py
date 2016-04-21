from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from itertools import *
from django.db import connection

# Create your views here.
def dictfetchall(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

def query_bookmark_by_user(request, username):
    query_string = "select a.username,b.title,b.description,b.url from auth_user a, marcador_bookmark b where a.id=b.owner_id and a.username=%s"
    cursor = connection.cursor()
    cursor.execute(query_string, username)
    # col_names = [desc[0] for desc in cursor.description]
    row = cursor.fetchone()
    #    if row is None:
    #        break
    #    row_dict = dict(izip(col_names, row))
    #    yield row_dict
    return render(request, 'marcador/bookmark_list.html',row)

def query_bookmark(request):
    # query_string = "select a.id,b.title,b.description,b.url from auth_user a, marcador_bookmark b where a.id=b.owner_id"
    query_string = "select b.title,b.url from auth_user a, marcador_bookmark b where a.id=b.owner_id"
    cursor = connection.cursor()
    cursor.execute(query_string)
    # col_names = [desc[0] for desc in cursor.description]
    # while True:
    #     row = cursor.fetchone()
    #     if row is None:
    #         break
    #     row_dict = dict(izip(col_names, row))
    #     yield row_dict
    # row = cursor.fetchone()
    rows = dictfetchall(cursor)
    context = {'bookmarks': rows}
    return render(request, 'marcador/query_results.html',context)

# def bookmark_list(request):
#     bookmarks = Bookmark.public.all()
#     context = {'bookmarks': bookmarks}
#     return render(request, 'marcador/bookmark_list.html', context)

# def bookmark_user(request, username):
#     user = get_object_or_404(User, username=username)
#     if request.user == user:
#         bookmarks = user.bookmarks.all()
#     else:
#         bookmarks = Bookmark.public.filter(owner__username=username)
#     context = {'bookmarks': bookmarks, 'owner': user}
#     return render(request, 'marcador/bookmark_user.html', context)

# def bookmark_custom(request)
#     bookmarks = Bookmark.public.all()
#     context = {'bookmarks': bookmarks}
#     return render(request, 'marcador/bookmark_list.html', context)
