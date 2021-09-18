# File describing the interactions with the database instance
# Class DBHandler implemented with Singleton pattern
# Abstracts the following operations:
#   - Initialisation of specific-purpose tables
#   - Updating rows in corresponding tables
#   - Showing existing records from tables

import sqlite3
from user import * 
from timeslot import *

class DBHandler:
##
##    object variables:
##      connection handler
##      cursor
##      
##

    def __init__(self):
        self._conn = sqlite3.connect('example.db')
        self._conn.row_factory = sqlite3.Row
        self._cursor = self._conn.cursor()
    
    ## Bootloader methods: Only called when program is created (one-use only)
    def bootloader(self):
        self.create_table_users()
        self.create_table_timeslots()

    def create_table_users(self):
        try:
            self._cursor.execute('CREATE TABLE users (username text, type text, bookings integer)')
        except:
            print("DBHandler Error: Could not create table 'users' ")

    def create_table_timeslots(self):
        try:
            self._cursor.execute('CREATE TABLE timeslots (slot_date date, author text, state text, attendees integer, max_capacity integer)')
        except:
            print("DBHandler Error: Could not create table 'timeslots' ")
    
    ## Database admin methods: Enters or removes rows from table
    def update_bookings(self, slot):
        self._cursor.execute("INSERT INTO timeslots VALUES (?, ?, ?, ?, ?)", ( slot.get_date() ,str(slot.get_author()), slot.get_state(), slot.get_attendees(), slot.get_capacity()))

    def update_user(self, user):
        if user.get_type() == "client":
            self._cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (user.get_user_name(), user.get_type(), user.get_booked_slots()) )
        elif user.get_type() == "author":
            self._cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (user.get_user_name(), user.get_type(), user.get_total_bookings()) )
        self._conn.commit()
    
    def terminate(self):
        self._conn.close()
        
    def remove_booking(self, slot):
        self._cursor.execute("DELETE FROM timeslots WHERE state = ?", ('available',))

    def remove_user(self, user):
        self._cursor.execute("DELETE FROM users WHERE username = ?", (user.get_user_name(),))
    # TODO: 
    # def remove_bookings(self, slot):
    # def remove_user(self, user):

    def update(self, *argv):
        for arg in argv:
            if type(arg) == Timeslot:
                self.update_bookings(arg)
            elif type(arg) == Client or type(arg) == Author:
                self.update_user(arg)

    

    def get_users(self):
        self._cursor.execute('SELECT * FROM users')
        users = self._cursor.fetchall()
        return users

    def get_timeslots(self):
        """
        returns all rows from timeslots schema
        """
        self._cursor.execute("SELECT * from timeslots") 
        timeslots = self._cursor.fetchall()
        return timeslots

    def print_bookings(self):
        for row in self._cursor.execute('SELECT * FROM timeslots'):
            print(row)
