#Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)and get fare information of train running under Indian Railways.

from random import randint  # importing randint to generate random train numbers

class Train:
    def __init__(self, train_number, train_name, total_seats):
        self.train_number = train_number
        self.train_name = train_name
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_ticket(self, num_seats):
        if self.booked_seats + num_seats <= self.total_seats:
            self.booked_seats += num_seats
            print(f"Successfully booked {num_seats} tickets.")
        else:
            print("Not enough available seats.")

    def get_status(self): 
        available_seats = self.total_seats - self.booked_seats
        print(f"Train Name: {self.train_name}")
        print(f"Train Number: {self.train_number}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Booked Seats: {self.booked_seats}")
        print(f"Available Seats: {available_seats}")

    def get_fare_info(self):
        fare_per_seat = 500  # Assume a fixed fare for simplicity
        total_fare = fare_per_seat * self.booked_seats
        print(f"Total Fare for {self.booked_seats} booked seats: {total_fare}")

# Example usage
train1 = Train("12345", "Express Train", 100)
train1.book_ticket(5)
train1.get_status()
train1.get_fare_info()