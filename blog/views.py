from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect

import sqlite3

def first(one):
    return one[0]


# Create your views here.

@csrf_protect
def post_list(request):
	
	
    conn = sqlite3.connect("/home/valdegg/Downloads/vidfangsefni.sqlite")
    c = conn.cursor()
	
    if(request.method == "POST"):
        dicto = request.POST 
		# dicto geymir web form inputið, hefur lykla, user_name, user_email og user_message
		# bæti við nýrri röð í töfluna
		
		
        try:
            c.execute("INSERT INTO listinn (Hugmynd, Utskyring, Hver)	 VALUES (?, ?, ?)", (dicto["title"], dicto["user_message"], dicto["user_name"]))
        except sqlite3.IntegrityError:
            print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))

        conn.commit()
			
	
    c.execute('SELECT Hugmynd  FROM listinn')
    hugmyndir = map(first,c.fetchall())
	
    c.execute('SELECT  Hugmynd, Utskyring, Hver  FROM listinn')
    allirdalkar = c.fetchall()
	
	
	
    return render(request, 'blog/post_list.html', {'hugmyndir': hugmyndir, 'allirdalkar': allirdalkar})
