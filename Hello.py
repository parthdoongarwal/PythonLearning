#this is the main branch


class Flight():
    def __init__(self , capicity ):
        self.capicity = capicity
        self.passengers = []

    def add_passengers(self , name):
        if len(self.passengers) < self.capicity:
            self.passengers.append(name)
            print("\nsucceseful booked. enjoy your flight")
        else:
            print("\nsorry looks the flight is booked\n")


flight = Flight(3)

# flight.add_passengers("Parth")
# flight.add_passengers("Yash")
# flight.add_passengers("Vansh")
# flight.add_passengers("Kim")
import sys

try:
    x = int(input("type a number: "))
    y = int(input("type a number: "))
except ValueError:
    print("\nlooks like you typed a letter insted of a number\n")
    sys.exit(1)

try:
    value = x / y
except ZeroDivisionError:
    print("\nError: cannot divide by zero\n")
    sys.error(1)

    
print(f"\n{x} / {y} = {value}\n")




