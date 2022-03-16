#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 11:59:57 2021

預約諮詢系統
"""
import datetime
class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
class Baby(Person):
    def speak(self):
        print('Blah vlah blah')
        
class Adult(Person):
    def speak(self):
        print('Hello, my name is %s' % self.first_name)
        
class Calender():
    def book_appointment(self, date):
        print('Booking appointment for date %s' % date)
        
class OrganizeAdult(Adult, Calender):
    pass

class OrganizeBaby(Baby, Calender):
    pass

andres = OrganizeAdult('Andres', 'Gomez')
boris = OrganizeBaby('Boris', 'Bumblebutton')

andres.speak()
boris.speak()
boris.book_appointment(datetime.date(2018,1,1))

class OrganizeBaby(Baby, Calender):
    def book_appointment(self, date):
        print('Note that you are booking an appointment with a baby.')
        super().book_appointment(date)
        
boris = OrganizeBaby('Boris', 'Bumblebutton')
boris.book_appointment(datetime.date(2018,1,1))        
    
    
       