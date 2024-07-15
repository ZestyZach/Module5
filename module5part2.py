books = int(input("Enter books purchased this month:\n"))
if(0 <= books < 2):
    points = 0
    print("Points earned:",points)
elif(2 <= books < 4):
    points = 5
    print("Points earned:",points)
elif(4 <= books < 6):
    points = 15
    print("Points earned:",points)
elif(6 <= books < 8):
    points = 30
    print("Points earned:",points)
elif(8 <= books):
    points = 60
    print("Points earned:",points)
else:
    print("Invalid Input(Please enter a positive number)")
    
input("Press Enter to exit.")