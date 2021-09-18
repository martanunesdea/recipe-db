# File describing the class Password
from timeslot import *

class User:
    def __init__(self, **kwargs):
        self._first_name = kwargs['first_name'] if 'first_name' in kwargs else 'example'
        self._last_name = kwargs['last_name'] if 'last_name' in kwargs else 'example'
        self._type = "user"

    def set_user_name(self, first_name, last_name):
        if first_name == 0 and last_name == 0:
            raise ArgumentError(f'Expected at least one argument to set the name of the user ')
        if first_name: # if argument is filled, set first name to that
            self._first_name = first_name
        if last_name:
            self._last_name = last_name
        return self._first_name + ' ' + self._last_name

    def get_user_name(self):
        return self._first_name + ' ' + self._last_name

    def __str__(self):
        return f'{self._first_name} {self._last_name}'

class Client(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._type = "client"
        self._bookings_booked = {0:'zero'}
        self._bookings_count = 0
       
    def get_type(self):
        return self._type

    def book_slot(self, slot):
        slot.add_booking()
        self._bookings_count += 1
        if self._bookings_booked[0] == 'zero':
            self._bookings_booked = {0 : slot}
        else:
            self._bookings_booked.update({ self._bookings_count: slot })

    def get_booked_slots(self):
        #print(f'User {self._first_name} has booking on {self._bookings} ')
        return self._bookings_count

class Author(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._type = "author"
        self._bookings_created = { 0:'zero'}
        self._bookings_count = 0

    def get_type(self):
        return self._type

    def get_total_bookings(self):
        return self._bookings_count

    def create_timeslot(self, date, state):
        slot = Timeslot(date, self, state)
        self._bookings_count += 1
        # get size of dictionary and then update it on list
        if self._bookings_created[0] == 'zero':
            self._bookings_created = {0 : slot}
        else:
            self._bookings_created.update({ self._bookings_count: slot })
        return slot

    # TODO: delete timeslot


    def get_bookings_created(self):
        return self._bookings_created

def main():
    if test():
        print("Test passed")
    else: 
        print("Test didn't pass")
    

def test():
    my_user = User(first_name = 'marta', last_name = 'nunes')
    print(my_user)
    return True


if __name__ == "__main__": main()