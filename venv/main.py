# Entry point for using the database manager 
# This will temporarily host the development code for the database manager
# The fully-featured and tested code will at a later stage make up the module "db_handler"

from db_handler import *
from user import * 
from timeslot import *

def main():
    my_author = Author(first_name = 'maria', last_name = 'pm')
    time1 = my_author.create_timeslot(date(2020, 10, 12), 'available')
    my_user = Client(first_name = 'marta', last_name = 'nunes')
    my_user.book_slot(time1)
    time2 = my_author.create_timeslot(date(2020, 12, 25), 'available')

    my_db = DBHandler()
    
    # On program startup, bootloader will create all tables necessary for execution
    # TODO: add ifdef-type conditional for bootloader mode 
    #my_db.bootloader() 
   
    #my_db.update(time1, my_author, my_user)
    my_db.update(my_author)
    my_db.update(time2)
    users_list = my_db.get_users() # print separately as these are different tables 
    print(users_list[0][0])   
    timeslots = my_db.get_timeslots()
    print(timeslots[0][0])
    my_db.print_bookings()
    my_db.remove_booking(time2)
    my_db.remove_user(my_author)
    print(users_list[0][0])
    my_db.terminate()


if __name__ == "__main__": main()