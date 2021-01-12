# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 2021 - 13:48
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 8 Classes and Object-Oriented Programming 

Encapsulation and Information hiding - Grades Class

@author: Atanas Kozarev - github.com/ultraasi-atanas
"""
class Grades(object):
    
    def __init__(self):
        """ Create empty grade book """
        self.students = []
        self.grades = {}
        self.isSorted = True
        
    def addStudent(self, student):
        """ Assumes: student is of type Student
            Add student to the grade book """
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
        
    def addGrade(self, student, grade):
        """ Assumes: grade is a float
            Add grade to the list of grades for student """
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')
    
    def getGrades(self, student):
        """ Return a list of grades for student """
        try: # return copy of list of student's grades
            return self.grades[student.getIdNum()][:]
        except: 
            raise ValueError('Student not in mapping')
        
    
    def getStudents(self):
        """ Return a stored list of the students in the grade book """
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:] #return copy of list of students
        
    def gradeReport(course):
        """ Assumes course is of type Grades """
        report = ''
        for s in course.getStudents():
            tot = 0.0
            numGrades = 0
            for g in course.getGrades(s):
                tot += g
                numGrades += 1
            try:
                average = tot/numGrades(s)
                report = report + '\n' + str(s) + '\'s mean grade is ' + str(average)
            except ZeroDivisionError:
                report = report + '\n' + str(s) + ' has no grades'
        
        return report
                