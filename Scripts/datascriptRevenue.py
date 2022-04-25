import django
import pandas as pd
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DATABASE.settings')

django.setup()
from RCRAS.models import *
#Reading data from excel
# df = pd.read_excel('Revenue.xlsx', sheet_name="Data")
# print(df)
# #Department_T
# df = df.drop_duplicates(subset=["Dept"])
# data = df.values.tolist()
# for i in data[0:16]:
#     if i[15] == "CSE" or i[15] == "cse" or i[15] == "EEE" or i[15] == "eee" or i[15] == "PhySci" or i[15] == "PHYSCI" or i[15] == "physci" or i[15] == "Physci":
#         schooltitlefk = School_T.objects.raw('''
#             SELECT SchoolTitle
#             FROM RCRAS_School_T
#             WHERE SchoolTitle = 'SETS'
#         ''')
#         dept = Department_T(DeptID=i[15], SchoolTitle=schooltitlefk[0])
#         dept.save()
# #Course_T
#     x=0
#     df = df.drop_duplicates(subset=["CourseID"])
#     data = df.values.tolist()
#     for i in data[0:]:
#         x+=1
#         print(x)
#         if pd.isna(i[1])==False:
#             course = Course_T(CourseID=i[1], CourseName=i[10],CreditHour=i[4])
#             course.save()


# # #CO_OFFERED_COURSE_T ,  CoOfferedCourseID 
# #             coList=i[2].split(",")
# #             for j in coList:
# #                 print(j)

# # #CO_OFFERED_COURSE_T 

# #             coList=i[2].split(",")
# #             for j in coList:

# #                 coCourse=CoOfferedCourse_T(CourseID=i[1],CoOfferedCourseID=j)
# #                 coCourse.save()

def populate(filename,sheet_name):
    # Reading data from excel
    #print(filename)
    df = pd.read_excel(filename, sheet_name=sheet_name)

# Department_T
    dfdept = df["Dept"].drop_duplicates()
    data = dfdept.values.tolist()
    for i in data:
        if i == "CSE" or i == "cse" or i == "EEE" or i == "eee" or i == "PhySci" or i == "PHYSCI" or i == "physci" or i == "Physci":
            schooltitlefk = School_T.objects.raw('''
                SELECT SchoolTitle
                FROM RCRAS_School_T
                WHERE SchoolTitle = 'SETS'
            ''')
            dept = Department_T(DeptID=i, SchoolTitle=schooltitlefk[0])
            dept.save()

        schooltitlefk1 = School_T.objects.raw('''
            SELECT SchoolTitle
            FROM RCRAS_School_T
            WHERE SchoolTitle IN ('SLASS','SBE','SPPH','SELS')
            ORDER BY SchoolTitle
        ''')
        dept2 = Department_T(DeptID="SBE", SchoolTitle=schooltitlefk1[0])
        dept3 = Department_T(DeptID="SELS", SchoolTitle=schooltitlefk1[1])
        dept4 = Department_T(DeptID="SLASS", SchoolTitle=schooltitlefk1[2])
        dept5 = Department_T(DeptID="SPPH", SchoolTitle=schooltitlefk1[3])
        dept2.save()
        dept3.save()
        dept4.save()
        dept5.save()
    return df    