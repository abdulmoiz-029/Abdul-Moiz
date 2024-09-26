def main():
    hotel = Hotel()
    
    while True:
        print("\n===== Hotel Management System =====")
        print("1. Add Room")
        print("2. Remove Room")
        print("3. Display Rooms")
        print("4. Reserve Room")
        print("5. Release Room")
        print("6. Save Rooms to File")
        print("7. Load Rooms from File")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            room_number = int(input("Enter room number: "))
            room_type = input("Enter room type: ")
            price = float(input("Enter price per night: "))
            room = Room(room_number, room_type, price)
            hotel.add_room(room)
        
        elif choice == '2':
            room_number = int(input("Enter room number to remove: "))
            hotel.remove_room(room_number)
        
        elif choice == '3':
            hotel.display_rooms()
        
        elif choice == '4':
            room_number = int(input("Enter room number to reserve: "))
            hotel.reserve_room(room_number)
        
        elif choice == '5':
            room_number = int(input("Enter room number to release: "))
            hotel.release_room(room_number)
        
        elif choice == '6':
            filename = input("Enter filename to save: ")
            hotel.save_rooms_to_file(filename)
        
        elif choice == '7':
            filename = input("Enter filename to load: ")
            hotel.load_rooms_from_file(filename)
        
        elif choice == '8':
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()
