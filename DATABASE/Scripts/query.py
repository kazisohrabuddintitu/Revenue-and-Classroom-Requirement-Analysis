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

def ClassSizeDistribution(Sem, Year, School):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT COUNT(*)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON deptcode=dept_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled BETWEEN 1 AND 10
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON deptcode=dept_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled BETWEEN 11 AND 20
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON deptcode=dept_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled BETWEEN 21 AND 30
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON deptcode=dept_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled BETWEEN 31 AND 35
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON deptcode=dept_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled BETWEEN 36 AND 40
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON deptcode=dept_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled BETWEEN 41 AND 50
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON deptcode=dept_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled BETWEEN 51 AND 55
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON deptcode=dept_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled BETWEEN 56 AND 60
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON deptcode=dept_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled > 60
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
        '''.format(Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School))
        result = cursor.fetchall()
    return result


# print(ClassSizeDistribution("Spring", '2021', "SETS"))
# sbe = ClassSizeDistribution("Spring", '2021', "SBE") 
# print(sbe)
# sels = ClassSizeDistribution("Spring", '2021', "SELS")
# sets = ClassSizeDistribution("Spring", '2021', "SETS")
# slass = ClassSizeDistribution("Spring", '2021', "SLASS")
# spph = ClassSizeDistribution("Spring", '2021', "SPPH")
# allarr = np.concatenate((sbe, sels, sets, slass, spph), axis=1)
# # # for i in allarr:
# # #     print(i)
# print(allarr)
# totalarr = allarr.sum(axis=1)
# print(totalarr)
# finalarr = np.concatenate((allarr,totalarr),axis=1)
# print(finalarr)

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

def EnrollmentBreakdownOfSchoolView(stuNo, school, year, semester):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT COUNT(*)
            FROM RCRAS_section_t AS s INNER JOIN RCRAS_course_t AS c ON s.SectionID = c.DeptID_id 
            INNER JOIN RCRAS_department_t AS d ON c.DeptID_id = d.DeptID
            WHERE s.SectionEnrolled = {} AND d.DeptID = "{}" AND Year= '{}' AND s.Semester= "{}"
        '''.format(stuNo, school, year, semester))
        result = cursor.fetchall()
    return result

# test = EnrollmentBreakdownOfSchool(5, "SBE", '2021', "Spring")
# test = str(test)[2:-3]
# test = int(test) + 1          
# print(test)

def AvailabilityAndCourseOfferingComparisonView(Sem, Year):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON DeptID=DeptID_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled BETWEEN 1 AND 20
            AND Semester = "{}" AND Year = '{}'
            -----------------------------------------------------------------------
            UNION ALL
            -----------------------------------------------------------------------
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON DeptID=DeptID_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled BETWEEN 21 AND 30
            AND Semester = "{}" AND Year = '{}'
            -----------------------------------------------------------------------
            UNION ALL
            -----------------------------------------------------------------------
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON DeptID=DeptID_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled BETWEEN 31 AND 35
            AND Semester = "{}" AND Year = '{}'
            -----------------------------------------------------------------------
            UNION ALL
            -----------------------------------------------------------------------
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON DeptID=DeptID_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled BETWEEN 36 AND 40
            AND Semester = "{}" AND Year = '{}'
            -----------------------------------------------------------------------
            UNION ALL
            -----------------------------------------------------------------------
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON DeptID=DeptID_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled BETWEEN 41 AND 50
            AND Semester = "{}" AND Year = '{}'
            -----------------------------------------------------------------------
            UNION ALL
            -----------------------------------------------------------------------
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON DeptID=DeptID_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled BETWEEN 51 AND 54
            AND Semester = "{}" AND Year = '{}'
            -----------------------------------------------------------------------
            UNION ALL
            -----------------------------------------------------------------------
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON DeptID=DeptID_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled BETWEEN 55 AND 64
            AND Semester = "{}" AND Year = '{}'
            -----------------------------------------------------------------------
            UNION ALL
            -----------------------------------------------------------------------
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON DeptID=DeptID_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled BETWEEN 65 AND 124
            AND Semester = "{}" AND Year = '{}'
            -----------------------------------------------------------------------
            UNION ALL
            -----------------------------------------------------------------------
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM RCRAS_department_t INNER JOIN RCRAS_course_t ON DeptID=DeptID_id
                INNER JOIN RCRAS_section_t ON CourseID=CourseID_id)
            WHERE SectionEnrolled BETWEEN 125 AND 168
            AND Semester = "{}" AND Year = '{}'
        '''.format(Sem, Year,Sem, Year,Sem, Year,Sem, Year,Sem, Year,Sem, Year,Sem, Year,Sem, Year,Sem, Year,Sem, Year))
        result = cursor.fetchall()
    return result

# test = AvailabilityAndCourseOfferingComparisonView("Spring", '2021')
# test = np.array(test)
# print(test)

def IUBavailableResources():
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT COUNT(*), (COUNT(*)*20)
            FROM RCRAS_Room_T
            WHERE RoomCapacity = 20
            ------------------------------
            UNION ALL
            ------------------------------
            SELECT COUNT(*), (COUNT(*)*30)
            FROM RCRAS_Room_T
            WHERE RoomCapacity = 30
            -----------------------------
            UNION ALL
            -----------------------------
            SELECT COUNT(*), (COUNT(*)*35)
            FROM RCRAS_Room_T
            WHERE RoomCapacity = 35
            -----------------------------
            UNION ALL
            -----------------------------
            SELECT COUNT(*), (COUNT(*)*40)
            FROM RCRAS_Room_T
            WHERE RoomCapacity = 40
            -----------------------------
            UNION ALL
            -----------------------------
            SELECT COUNT(*), (COUNT(*)*50)
            FROM RCRAS_Room_T
            WHERE RoomCapacity = 50
            -----------------------------
            UNION ALL
            -----------------------------
            SELECT COUNT(*), (COUNT(*)*54)
            FROM RCRAS_Room_T
            WHERE RoomCapacity = 54
            -----------------------------
            UNION ALL
            -----------------------------
            SELECT COUNT(*), (COUNT(*)*64)
            FROM RCRAS_Room_T
            WHERE RoomCapacity = 64
            -----------------------------
            UNION ALL
            -----------------------------
            SELECT COUNT(*), (COUNT(*)*124)
            FROM RCRAS_Room_T
            WHERE RoomCapacity = 124
            -----------------------------
            UNION ALL
            -----------------------------
            SELECT COUNT(*), (COUNT(*)*168)
            FROM RCRAS_Room_T
            WHERE RoomCapacity = 168
        ''')
        result = cursor.fetchall()
    return result

# test = IUBavailableResources()
# test = np.array(test)
# print(test)   