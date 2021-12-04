'''
Write a Python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:

The ticket number should be generated as airline:src:dest:number where

1. Consider AL1 as the value for airline
2. src and dest should be the first three characters of the source and destination cities.
3. number should be auto-generated starting from 101

The program should return the list of ticket numbers of last five passengers.
Note: If passenger count is less than 5, then return the list of all generated ticket numbers.
'''

#inputting--------------------------------------------------------------------------------------------------------------
try:
    airline = "AL1"
    print("-"*50)
    src = input("Please enter source city          : ")
    dest = input("Please enter destination city     : ")
    no_of_passangers = int(input("Please enter number of passangers : "))

#formatting-------------------------------------------------------------------------------------------------------------
    src = src.upper()
    dest = dest.upper()

#starting function if src and dest contains only alphabets--------------------------------------------------------------
    if(src.isalpha() and dest.isalpha()):
        def flight_tickets(airline,src,dest,no_of_passangers):
            first_ticket = 101
            ticket = []
            counter = 1

            while(counter <= no_of_passangers):
                ticket.append(airline + ":" + src[:3] + ":" + dest[:3] + ":" + str(first_ticket))
                first_ticket += 1
                counter += 1

            return ticket

        ticket_number = flight_tickets(airline,src,dest,no_of_passangers)

        print("-"*50)
        if(len(ticket_number) < 5):
            for ticket in ticket_number:
                print(ticket)

        else:
            for ticket in ticket_number[-5:]:
                print(ticket)
        print("-" * 50)

#exceptions-------------------------------------------------------------------------------------------------------------
    else:
        print("-"*50)
        print("Please enter the name of city in letters only")
        print("-" * 50)

except ValueError:
    print("-"*50)
    print("Please enter number of passangers in numbers only")
    print("-" * 50)