def book_room(bookings):
    room_no=(input("enter your room number:"))
    if room_no in bookings:
        print("Room number is already booked")
    else:
        
        guest_name = input("Enter Guest name:")
        room_type = input("Enter Room_Type: Eg.,Deluxe,Standard,Suite")
        days=int(input("Enter number of days:"))
        total_price = float(input("Enter Total_Price"))
        
        bookings[room_no]={
            
            "Room_Number": room_no,
             "Guest_Name" :guest_name,
             "Room_Type" : room_type,
             "Days":days,
             "Total_Price":total_price    
            } 
        
        print("Room booked succesfully")
def view_bookings(bookings):
    for room_no,details in bookings:
        print("Room_No:",room_no)
        print("Guest_Name:",details["guest_name"])
        print("Room_Type:",details["room_type"])
        print("Number of days:",details["days"])
        print("Total_Price:",details["total_price"])
            
    if len(bookings)==0:
        print("No booking  Records Found")
    else:
        print("Booking Details")
def search_booking(bookings):
    romm_no = input("Enter Room Number:")
    if room_no in bookings.items():
        print("Booking Found")
        print("Room_Number:",room_no)
        print("Guest_Name:",bookings[room_no]["Guest Name"])
        print("Room Type:",bookings[room_no]["Room_Type"])
        print("Number of days:",bookings[room_no]["Days"])
        print("Total_Price:",bookings[room_no]["total_price"])
    else:
        print("Booking not Found.")

def update_days(bookings):
    room_no= input("Enter Room Number:")
    if room_no in bookings:
       new =int(input("Enter new number of stay days ")) 
       bookings[room_no][Days]==new
       print("Booking Days updated succesfully")
    else:
        print("Booking not Found")
        
def cancel_booking(bookings):
    room_no = input("Enter room Number:")
    if room_no in bookings:
       del bookings[room_no]
       print("Booking cancelled Succesfully")     
    else:
        print("Booking not Found")
        
while True:
    print("\nMenu")
    print("1.Book Room")
    print("2.View All Bookings")
    print("3.Search Booking")
    print("4.Update Booking Days")
    print("5.Cancel Booking")
    print("6.Exit")
    
    choice =int(input("enter your choice:"))
    if choice==1:
       book_room(bookings)
    elif choice==2:
       view_bookings(bookings)
    elif choice == 3:
        search_booking(bookings)
    elif choice == 4:
        update_days(bookings)
    elif choice == 5:
        cancel_booking(bookings) 
    elif choice == 6:
        print("EXIT")
        break
    else:
        print("INVALID CHOICE")       
        
        
        
            
           
    

           
          
            

    
        
            
            
            
            
            
            
    
