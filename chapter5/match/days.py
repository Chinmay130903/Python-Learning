Number_of_Days=int(input("enter number of days"))

day=Number_of_Days%7
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday") 
    case 4:
        print("thrusday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 0:
        print("sunday")
   
