import datetime



def main():
    age = input("Please enter a date in the following format xx-xx-xxxx : ")
   
    
    if age[2] == "-" and age [5] == "-" and len(age) == 10 :
        if int(age[0:2]) >= 0 and int(age[0:2]) < 32 : 
            day = int(age[0:2])
        else:
            raise Exception("Not a date")
        if int(age[3:5]) > 0 and int(age[3:5]) <= 12 : 
            month = int(age[3:5])
        else:
            raise Exception("Not a date")
        if int(age[3:5]) > 0 and int(age[3:5]) <= 12 : 
            year = int(age[6:])
        else:
            raise Exception("Not a date")
    else:
        raise Exception("Not a date")
    
    
    current = datetime.date.today()
    years = current.year - year
    if current.month < month or (current.month == month and current.day < day):
        years -= 1
    print(years)
    
    
        


if __name__ == "__main__":
    main()