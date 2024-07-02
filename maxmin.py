import datetime



def main():
    numbers = input("Please enter a list of numbers :").replace("[","")
    numbers = numbers.replace("]","")
    
    
    listNum = [int(x) for x in numbers.split(',')]
            
    largest  = listNum[0]
    smallest = listNum[0]
    
    for num in listNum:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
            
    
    print("[{},{}]".format(smallest,largest))
    
    
    
if __name__ == "__main__":
    main()