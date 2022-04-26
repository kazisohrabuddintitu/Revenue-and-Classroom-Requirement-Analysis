from django.db import connection
import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
import sys
sys.path.append(PROJECT_PATH)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DATABASE.settings')
import django
django.setup()
from RCRAS.models import *

# with connection.cursor() as c:
#     c.execute('''
#     CREATE OR REPLACE VIEW joinedtable AS
#     SELECT *
#     FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
#                                INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id
#     ''')
    
def enrollment_wise_course_school(School, Sem, Year):
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 1 AND 10
        UNION ALL
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 11 AND 20
        UNION ALL
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 21 AND 30
        UNION ALL
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 31 AND 35
        UNION ALL
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 36 AND 40
        UNION ALL
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 41 AND 50
        UNION ALL
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 51 AND 55
        UNION ALL
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 56 AND 60
        UNION ALL
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled > 60
        '''.format(School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year))

        col = cursor.fetchall()
    return col
 
 #SELECT SUM(Sec.SectionEnrolled*Crs.CreditHour) AS Total
   #    FROM RCRAS_section_t AS Sec, RCRAS_course_t AS Crs, RCRAS_department_t AS #Dept, RCRAS_school_t AS Schl
   #    WHERE Sec.CourseID=Crs.CourseID, Cour.DeptID=Dept.DeptID AND Dept.SchoolTitle=Schl.SchoolTitle AND
    #   Year={} AND Semester="{}" AND Schl.SchoolTitle="{}"
def iub_revenue(Yearfrom, Yearto, School):
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT Year,Semester,SUM(groupbycredit.sum)
        FROM
            (
                SELECT COUNT(*),credithour, SUM( SectionEnrolled), credithour*SUM( SectionEnrolled) AS sum, Semester,year
                FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
                WHERE Semester IN ("Spring","AUTUMN","SUMMER") AND Year BETWEEN {} AND {} AND SchoolTitle_id = "{}"
                GROUP BY Year,Semester,Credithour
            ) AS groupbycredit
        GROUP BY Year,Semester
        ORDER BY Year, FIELD (Semester,"Spring","Summer","Autumn");
        '''.format(Yearfrom, Yearto, School))

        col = cursor.fetchall()

    return col

    