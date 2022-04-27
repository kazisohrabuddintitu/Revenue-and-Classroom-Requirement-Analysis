
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
from operator import itemgetter
import numpy as np
from os import walk

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

        list10.append(sum(list9))
        list10.append(sum(list1))
        list10.append(sum(list2))
        list10.append(sum(list3))
        list10.append(sum(list4))
        list10.append(sum(list5))
        list10.append(sum(list6))
        list10.append(sum(list7))
        list10.append(sum(list8))
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


def view_availabilityvscourse_offer(request):
    if request.method == 'POST':

        semester = request.POST.getlist('sem')
        year = request.POST.get('year')

        roomsize = roomsizelist()
        roomsize = [element for tupl in roomsize for element in tupl]
        class6 = []
        for i in semester:
            sections = classroom_requirement_course_offer(i, year)
            class6temp = []
            for j in sections:
                class6temp.append(float("{:.2f}".format(j/12)))
            class6.append(class6temp)
        # #print(class6)
        # sumcls6 = "{:.2f}".format(sum([float(i) for i in class6]))
        listOddsize = roomsize[::2]
        # ulta ache. odd ->even, even-> odd e ase.
        listEvensize = roomsize[1::2]
        class6offered = []
        for j in range(0, len(semester)):
            a = []
            b = []
            c = []
            d = []
            e = []
            f = []
            g = []
            c6 = []
            r = class6[j][0]
            s = class6[j][1]
            t = class6[j][2]
            u = class6[j][3]
            v = class6[j][4]
            w = class6[j][5]
            x = class6[j][6]
            y = class6[j][7]
            k = 0
            l = 0
            for i in range(0, len(listOddsize)):

                if listOddsize[i] in range(1, 21):
                    # #print(listOddsize[i])
                    # #print(r+s)
                    a.append(r+s)

                if listOddsize[i] in range(21, 31):
                    # #print(listOddsize[i])
                    # #print(t)
                    b.append(t)

                if listOddsize[i] in range(31, 36):
                    # #print(listOddsize[i])
                    # #print(u)
                    c.append(u)

                if listOddsize[i] in range(36, 41):
                    # #print(listOddsize[i])
                    # #print(v)
                    d.append(v)

                if listOddsize[i] in range(41, 51):
                    # #print(listOddsize[i])
                    # #print(w)
                    e.append(w)

                if listOddsize[i] in range(51, 56):
                    # #print(listOddsize[i])
                    # #print(x)
                    f.append(x)

                if listOddsize[i] in range(56, 65):
                    # #print(listOddsize[i])
                    # #print(y)
                    g.append(y)

            c6 = a+b+c+d+e+f+g
            if len(f) == 0:
                listOddsize.append(54)
                listEvensize.append(0)
                c6.append(x)
            if len(g) == 0:
                listOddsize.append(64)
                listEvensize.append(0)
                c6.append(y)

            #c6.insert(0,sum(c6))

            class6offered.append(c6)
            c6 = []
            a = []
            b = []
            c = []
            d = []
            e = []
            f = []
            g = []

        totalroom = listEvensize
        #totalroom.insert(0,sum(listEvensize))
        chartdata = []
        chartlabel = listOddsize
        chartdata += class6offered  # +[totalroom]
        #print(class6offered)
        #print(listEvensize)

        #table start->
        temptable = []
        tablelabel = []
        rowlentemp = len(listOddsize)
        tablelabel += listOddsize
        tablelabel.append('Total')
        resource = listEvensize
        difference = []
        for i in range(0, len(semester)):
            for j in range(len(listEvensize)):
                difference.append(float("{:.2f}".format(
                    listEvensize[j]-class6offered[i][j])))

        difference = [difference[i:i+rowlentemp]
                      for i in range(0, len(difference), rowlentemp)]
        temptable.append(resource)
        for i in range(0, len(semester)):
            temptable.append(class6offered[i])
            temptable.append(difference[i])

        # https://numpy.org/doc/stable/reference/generated/numpy.transpose.html
        table = np.transpose(temptable)
        # https://www.delftstack.com/howto/numpy/sum-of-columns-matrix-numpy/
        total = np.sum(table, axis=0)

        # https://stackoverflow.com/questions/2762058/format-all-elements-of-a-list
        total = ["%.2f" % member for member in total]
        # https://www.codegrepper.com/code-examples/python/add+row+to+numpy+2+dimension+arrayhttps://www.codegrepper.com/code-examples/python/add+row+to+numpy+2+dimension+array
        table = np.append(table, [total], axis=0)

        # https://moonbooks.org/Articles/How-to-add-a-new-column-in-a-table-using-python-and-numpy-/
        finaltable = np.c_[tablelabel, table]

        # # #https://stackoverflow.com/questions/12575421/convert-a-1d-array-to-a-2d-array-in-numpy
        # # differencematrix=np.reshape(difference,(-1, len(semester)))

        ##print(finaltable)

        return render(request, 'availabilityvscourse.html', {
            'schools': schoolList,
            'semesters': semesterlist,
            'years': yearlist,
            'chartdata': chartdata,
            'chartlabel': chartlabel,
            'selectedsem': semester,
            'noofcols': 2+len(semester)*2,
            'resource': listEvensize,
            'table': finaltable,
            'search': 0,
            'segment': 'usage',
        })

    else:
        return render(request, 'availabilityvscourse.html', {
            'schools': schoolList,
            'semesters': semesterlist,
            'years': yearlist,
            'search': 1,
            'segment': 'usage',
        })


def view_revenue_of_iub(request):
    if request.method == 'POST':
        school = request.POST.getlist('scl')
        yearf = request.POST.get('year1')
        yeart = request.POST.get('year2')
        #print(school, yearf, yeart)
        revenue = []
        for i in school:
            revenue.append(iub_revenue(yearf, yeart, i))
        # #print(revenue)
        a = abs(int(yearf)-int(yeart))+1
        # #print(type(a))

        list1 = []
        list2 = []
        list3 = []
        total = []

        for j in revenue:
            for i in j:
                list1.append(str(i[0])+i[1])
                list2.append(int(i[2]))
        list1 = list(dict.fromkeys(list1))
        list2 = [list2[i:i+a*3] for i in range(0, len(list2), a*3)]

        # #print(list1)
        # #print(list2)
        return render(request, 'revenueofiub.html', {
            'schools': schoolList,
            'yearfrom': yearlist,
            'yearto': yearlist,
            'selectedschool': school,
            'revenuesemyear': list1,
            'revenue': list2,

            'search': 0,
            'segment': 'rev',
        })

    else:
        return render(request, 'revenueofiub.html', {
            'schools': schoolList,
            'yearfrom': yearlist,
            'yearto': yearlist,
            'search': 1,
            'segment': 'rev',
        })   
        
def view_usage_resource(request):
    if request.method == 'POST':
        sem = request.POST.getlist('sem')
        year = request.POST.get('year')
        table = []
        total = []
        table2 = []
        t2r1 = ['Average of ROOM_CAPACITY']
        t2r2 = ['Average of ENROLLED']
        t2r3 = ['Average of Unused Space']
        t2r4 = ['Unused Percent %']
        selectedsem = '| '
        for i in sem:
            sbe = resources_usage('SBE', i, year)
            sels = resources_usage('SELS', i, year)
            sets = resources_usage('SETS', i, year)
            slass = resources_usage('SLASS', i, year)
            spph = resources_usage('SPPH', i, year)
            selectedsem += i+' '+year+' | '

            # touple of touple to list
            sbe = [float("%.2f" % (element))
                   for tupl in sbe for element in tupl]
            # https://stackoverflow.com/questions/3204245/how-do-i-convert-a-tuple-of-tuples-to-a-one-dimensional-list-using-list-comprehe
            # https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
            sels = [float("%.2f" % (element))
                    for tupl in sels for element in tupl]
            sets = [float("%.2f" % (element))
                    for tupl in sets for element in tupl]
            slass = [float("%.2f" % (element))
                     for tupl in slass for element in tupl]
            spph = [float("%.2f" % (element))
                    for tupl in spph for element in tupl]

            totala = sbe[0]+sels[0]+sets[0]+slass[0]+spph[0]
            totalb = sbe[1]+sels[1]+sets[1]+slass[1]+spph[1]
            totalc = sbe[2]+sels[2]+sets[2]+slass[2]+spph[2]
            totald = sbe[3]+sels[3]+sets[3]+slass[3]+spph[3]
            totale = sbe[4]+sels[4]+sets[4]+slass[4]+spph[4]

            t2r1.append("%.2f" % (totalb/5))
            t2r2.append("%.2f" % (totalc/5))
            t2r3.append("%.2f" % (totald/5))
            t2r4.append("%.2f" % (totale/5))

            total.append([i, totala, "%.2f" % (totalb/5), "%.2f" %
                         (totalc/5), "%.2f" % (totald/5), "%.2f" % (totale/5)])

            sbe.insert(0, 'SBE')
            sels.insert(0, 'SELS')
            sets.insert(0, 'SETS')
            slass.insert(0, 'SLASS')
            spph.insert(0, 'SPPH')

            total.append(sbe)
            total.append(sels)
            total.append(sets)
            total.append(slass)
            total.append(spph)
        #print(total)
        table += total
        table2 = [t2r1]+[t2r2]+[t2r3]+[t2r4]
        total = []
        #print(table2)
        return render(request, 'resourceusage.html', {
            'semesters': semesterlist,
            'years': yearlist,
            'table': table,
            'table2': table2,
            'selectedsem': selectedsem,
            'selectedyear': year,
            'semfort2': sem,
            'rowsize': len(sem)+1,
            'search': 0,
            'segment': 'usage',

        })

    else:
        return render(request, 'resourceusage.html', {
            'semesters': semesterlist,
            'years': yearlist,
            'search': 1,
            'segment': 'usage',
        })  
        
