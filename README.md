# booking_app
This repository was designed to create a booking system, stored on a database server. The end goal is to connect this system with a front-end web application for ease of use of the booking system.

The user requirements for this booking system may change over time, but the scope of this project will include:

- Keeping a calendar
- Having the concept of **a collection of timeslots** within the calendar. These timeslots may have two **states**: **available** or **fully booked**/**not available.**
- The timeslots become "not available" once they have reached a **maximum booking capacity**.
- Having the concept of **client** **user** and **admin user**, where admin is the person that creates, deletes and views the timeslots and user is the person that views and books timeslots.
- The **admin** may **set** or **edit** the **maximum booking capacity** of the timeslots, which will in turn change the **state** of the timeslot. In this project it will be out of scope for admin users to add new properties to the timeslots.
- The calendar must be printed out somewhere.

New points to build on:

- The calendar must be shown on a webpage.
- Both type of users require authentication to access the booking system.
- The booking system will notify the timeslot **creator** (ie. an admin user) when a timeslot was booked.
- Allow admin users to add properties to the timeslots created.
