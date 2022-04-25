
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login

from django.http import request
from django.http.response import HttpResponseRedirect
from RCRAS.models import *
import numpy as np
from numpy.lib.function_base import diff
from DATABASE.settings import BASE_DIR
from Scripts.query import *
from operator import itemgetter
import numpy as np
from subprocess import run
import sys

semesterlist = ["Spring", "Summer", "Autumn"]
yearlist = [2009, 2010, 2011, 2012, 2013, 2014,
            2015, 2016, 2017, 2018, 2019, 2020, 2021]
# yearlist = [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014,
#             2013, 2012, 2011, 2010, 2009]
schoolList = ['SBE', 'SELS', 'SETS', 'SLASS', 'SPPH']
SETSdeptList = ['CSE', 'EEE', 'PhySci']

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        #check if the user has entered correct credentitals
        user = authenticate(username=username, password=password)

        if user is not None:
            #A backend authenticated the credentials
            login(request, user)
            return render(request,"index.html")
        else:
            #No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
    
def revenue(request):
    return render(request,'revenue.html')

def about(request):
    return render(request,'about.html')

def view_classroom_requirement_course_offer(request):

    if request.method == 'POST':
        #semester = semesterlist[int(request.POST.get('sem'))]
        #year = yearlist[int(request.POST.get('year'))]
        lbl = ['1-10', '11-20', '21-30', '31-35',
               '36-40', '41-50', '51-55', '56-65']

        semester = request.POST.get('sem')
        year = request.POST.get('year')
        sections = classroom_requirement_course_offer(semester, year)
        selectedsem = semester+' '+year
        table = []
        class6 = []
        # print(sections)
        sumsections = sum(sections)
        for i in sections:
            class6.append("{:.2f}".format(i/12))
        # print(class6)

        sumcls6 = "{:.2f}".format(sum([float(i) for i in class6]))

        class7 = []
        for i in sections:
            class7.append("{:.2f}".format(i/14))
        # print(class7)
        sumcls7 = "{:.2f}".format(sum([float(i) for i in class7]))

        for i in range(len(lbl)):
            col1 = lbl[i]
            col2 = sections[i]
            col3 = class6[i]
            col4 = class7[i]
            table.append([col1, col2, col3, col4])
        table.append(['Total', sumsections, sumcls6, sumcls7])
        # print(class6)

        str1 = semester+" "+str(year)
        return render(request, 'classroom_requirment.html', {
            'semesters': semesterlist,
            'years': yearlist,
            'class6': class6,
            'class7': class7,
            'sections': sections,
            'seme': str1,
            'table': table,
            'selectedsem': selectedsem,


            'search': 0,
            'segment': 'cls_req',
        })

    else:
        return render(request, 'classroom_requirment.html', {
            'semesters': semesterlist,
            'years': yearlist,
            'segment': 'cls_req',
            'search': 1,
        })