users = []

while True:
    print("1. Show Users")
    print("2. Add User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")
    choice = input("Choose (1-5): ")
    
    if choice == "1":
        print(users if users else "No Users Found. Try Again.")
        
    elif choice == "2":
        users.append(input("Enter User Name: "))
        print("User Added Successfully.")
        
    elif choice == "3":
        print(f"Current Users: {users}")
        try:
            i = int(input("Enter Index to Update: "))
            if 0 <= i < len(users):
                users[i] = input("Enter New Name: ")
                print("User Updated Successfully.")
            else:
                print("Invalid Index.")
        except ValueError:
             print("Please Enter a Valid Number.")
             
           
    elif choice == "4":
        print(f"Current Users: {users}")
        try:
             i = int(input("Enter Index to Delete: "))
             if 0 <= i < len(users):
                 users.pop(i)
                 print("User Deleted Successfully.")
             else:
                 print("Invalid Index")
        except ValueError:
              print("Please Enter a Valid Number.")
              
    elif choice == "5":
        print("Exiting.... Thank You!")
        break
         
    else:
        print("Invalid Choice. Please  pick again (1-5).")