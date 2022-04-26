
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
from Scripts import query
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

def view_enrolment_course_school(request):
    if request.method == 'POST':
        l = ['1-10', '11-20', '21-30', '31-35', '36-40',
             '41-50', '51-55', '56-60', '60+']
        school = request.POST.getlist('scl')
        semester = request.POST.get('sem')
        year = request.POST.get('year')
        selectedsem = semester+' '+year
        rowsize = len(school)+2
        enrollment = []
        labels = []

        for i in school:

            enrollment.append(enrollment_wise_course_school(i, semester, year))

        for j in l:
            for i in school:
                labels.append(i+':'+j)

        #enrollment = [item for t in enrollment for item in t for item in item]

        list0 = []
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list9 = []
        list10 = []
        table = []
        for i in enrollment:
            e = [item for t in i for item in t]
            list0.append(e)
            list9.append(e[0])
            list1.append(e[1])
            list2.append(e[2])
            list3.append(e[3])
            list4.append(e[4])
            list5.append(e[5])
            list6.append(e[6])
            list7.append(e[7])
            list8.append(e[8])

        list10.append(sum(list1))
        list10.append(sum(list2))
        list10.append(sum(list3))
        list10.append(sum(list4))
        list10.append(sum(list5))
        list10.append(sum(list6))
        list10.append(sum(list7))
        list10.append(sum(list8))
        list10.append(sum(list9))

        temprow = []
        for i in range(len(l)):
            temprow = [row[i] for row in list0]
            temprow.append(list10[i])
            temprow.insert(0, l[i])
            table.append(temprow)  # make row wise

        list0.insert(0, list10)
        # table.append([row[0] for row in list0].insert(0,'Total'))#add total to end of the list
        #print(table)
        return render(request, 'enrollmentwise.html', {
            'schools': schoolList,
            'selectedschool': school,
            'rowsize': rowsize,
            'selectedsem': selectedsem,
            'semesters': semesterlist,
            'years': yearlist,
            'table': table,
            'enrollment': list0,
            'labels': labels,
            'search': 0,
            'segment': 'enroll',
        })

    else:
        return render(request, 'enrollmentwise.html', {
            'schools': schoolList,
            'semesters': semesterlist,
            'years': yearlist,
            'segment': 'enroll',
            'search': 1,
        })

def EnrollmentBreakdownOfSchoolView(request):
    if request.method == "POST":
        semester = request.POST['semester']
        year = request.POST['year']
        strr = semester + " " + year

        collabel = ["Enrollment", "SBE", "SELS", "SETS", "SLASS", "SPPH", "Total"]
        table = [collabel]
        rowlabel = []
        
        for i in range(62):
            num = i+1
            rowlabel.append(f'{num}')
        rowlabel.append('Total')

        sbet = 0
        selst = 0
        setst = 0
        slasst = 0
        sppht = 0
        totalt = 0
        
        for i in range(63):
            n = i+1
            sbe = query.EnrollmentBreakdownOfSchoolView(n, "SBE", year, semester)
            sels = query.EnrollmentBreakdownOfSchoolView(n, "SELS", year, semester)
            sets = query.EnrollmentBreakdownOfSchoolView(n, "SETS", year, semester)
            slass = query.EnrollmentBreakdownOfSchoolView(n, "SLASS", year, semester)
            spph = query.EnrollmentBreakdownOfSchoolView(n, "SPPH", year, semester)

            sbe = str(sbe)[2:-3]
            sels = str(sels)[2:-3]
            sets = str(sets)[2:-3]
            slass = str(slass)[2:-3]
            spph = str(spph)[2:-3]

            total =  int(sbe) + int(sels) + int(sets) + int(slass) + int(spph)
            
            sbet += int(sbe)
            selst += int(sels)
            setst += int(sets)
            slasst += int(slass)
            sppht += int(spph)
            totalt += total
            
            if n == 63:
                table.append([rowlabel[i], sbet, selst, setst, slasst, sppht, totalt])
            else:
                table.append([rowlabel[i], sbe, sels, sets, slass, spph, total])

        return render(request, 'EnrollmentBreakdownOfSchoolView.html', {
            'semesterList':semesterlist,
            'yearList': yearlist,
            'str': strr,
            'table': table,

        })

    else:
        return render(request, 'EnrollmentBreakdownOfSchoolView.html', {
            'semesterList':semesterlist,
            'yearList': yearlist,
        })

def AvailabilityAndCourseOfferingComparisonView(request):
    if request.method == "POST":
        semester1 = request.POST['semester1']
        year = request.POST['year']
        semester2 = request.POST['semester2']
        strr = semester1 + " and " + semester2 + " in " + year

        arr = query.IUBavailableResources()
        arr = np.array(arr)
        sem1 = query.AvailabilityAndCourseOfferingComparisonView(semester1, year)
        sem1 = np.array(sem1)
        sem2 = query.AvailabilityAndCourseOfferingComparisonView(semester2, year)
        sem2 = np.array(sem2)

        sem1 = sem1.flatten()         
        sem2 = sem2.flatten()
        collabel = ["Class size", "IUB resource", semester1, "Difference", semester2, "Difference"]
        rowlabel = ["20", "30", "35", "40", "50", "54", "64", "124", "168", "Total"]

        count = 0
        iubt = 0
        sem1t = 0
        sem2t = 0
        diff1t = 0
        diff2t = 0
        table = [collabel]

        iublist = []
        for item1, item2 in arr:
            diff1 = item1 - sem1[count]
            diff2 = item1 - sem2[count]

            iubt+=item1
            sem1t+= sem1[count]
            sem2t+= sem2[count]
            diff1t += diff1
            diff2t += diff2
            iublist.append(item1)
            table.append([ rowlabel[count], item1, sem1[count], "{:.2f}".format(diff1), sem2[count], "{:.2f}".format(diff2) ])  
            count+=1

        table.append([rowlabel[9], "{:.2f}".format(iubt), "{:.2f}".format(sem1t), "{:.2f}".format(diff1t), "{:.2f}".format(sem2t), "{:.2f}".format(diff2t) ])
        labels = ["20", "30", "35", "40", "50", "54", "64", "124", "168"]

        return render(request, 'AvailabilityAndCourseOfferingComparisonView.html', {
            'semesterList':semesterlist,
            'yearList': yearlist,
            'str': strr,
            'table': table,
            'iub': iublist,
            'datavalues1': sem1,
            'datavalues2': sem2,
            'labels': labels,
            'Semester1': semester1,
            'Semester2': semester2,

        })

    else:
        return render(request, 'AvailabilityAndCourseOfferingComparisonView.html', {
            'semesterList':semesterlist,
            'yearList': yearlist,
        })

    
