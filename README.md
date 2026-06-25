# Airline Reservation System

A simple Airline Reservation System built using Python and MySQL. This project was created to manage flight details, passenger information, and ticket bookings through a menu-driven interface.

## About the Project

The system allows users to perform basic airline management operations such as:

- Adding, updating, and deleting flights
- Managing passenger records
- Creating and managing bookings
- Viewing all available records
- Searching booking details using passenger ID

The project uses MySQL as the backend database and Python for handling user interactions and database operations.

## Features

### Flight Management
- Add new flights
- Update flight information
- Delete flight records
- View all flights

### Passenger Management
- Add passenger details
- Update passenger records
- Delete passenger records
- View all passengers

### Booking Management
- Create new bookings
- Update booking details
- Cancel bookings
- View all bookings
- Search bookings by passenger ID

## Technologies Used

- Python
- MySQL
- mysql-connector-python

## Database Tables

The project works with the following tables:

- Flights
- Passengers
- Bookings

These tables are connected to manage airline reservations efficiently.

## How to Run

1. Install Python.
2. Install MySQL Server.
3. Create the required database and tables.
4. Install MySQL Connector:

```bash
pip install mysql-connector-python
```

5. Update the database credentials in the Python file if needed.

```python
host='localhost'
user='root'
passwd='your_password'
database='Flight_Booking_System'
```

6. Run the program:

```bash
python airline_reservation.py
```

## Sample Menu

```text
1. Add Flight
2. Delete Flight
3. Update Flight
4. Add Passenger
5. Delete Passenger
6. Update Passenger
7. New Booking
8. Delete Booking
9. Update Booking
10. Show Flights
11. Show Passengers
12. Show Bookings
13. Search Record
14. Exit
```

## Learning Outcomes

Through this project, I learned:

- Connecting Python with MySQL databases
- Performing CRUD operations
- Writing SQL queries inside Python
- Handling user input in menu-driven applications
- Managing relationships between different database tables

## Future Improvements

- Graphical User Interface (GUI)
- User authentication system
- Online ticket payment integration
- Flight seat availability tracking
- Better error handling and validation

## Author

Created as a database management and Python learning project.
