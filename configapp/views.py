from django.shortcuts import render

# Create your views here.
from .models import *

def S_01(request):
    students=Student.objects.all()
    kurs = Kurs.objects.all()


    st_1={
        'kursning': kurs,
        'studentning':students,
        'title':'Student title'
    }

    return render(request, 'st_index.html',context=st_1 )

def K_01(request):
    kurs = Kurs.objects.all()
    students = Student.objects.all()

    ku_1={
        'studentning': students,
        'kursning':kurs,
        'title':'Kurs title'
    }

    return render(request, 'kr_index.html', context=ku_1)