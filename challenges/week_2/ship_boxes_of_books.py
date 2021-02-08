def main():
    bigBoxH=float(input("Enter big box height in inches: "))
    smallBoxH=float(input("Enter small box height in inches: "))
    bookH=float(input("Enter book height in inches: "))
    noOfBooks=float(input("Enter number of books: "))
    temp1=bigBoxH//bookH
    noOfBigBox=noOfBooks//temp1
    temp2=smallBoxH//bookH
    noOfSmallBox=noOfBooks//temp1
    if noOfBigBox==0 and noOfSmallBox==0:
        print("Ship 1 small box or ship 1 big box ")
        return
    remBooks=noOfBooks%temp1
    noOfSmallBox=(remBooks//temp2)
    if (remBooks%smallBoxH)<0:
        noOfSmallBox+=1
    res="Ship "+str(int(noOfBigBox))+" big box \nShip "+str(int(noOfSmallBox))+" small box"
    print(res)
if __name__=="__main__":
    main()

    
PSEUDOCODE

    """
program start 
    bigBoxH = input prompt user convert the users input to float
    smallBoxH = input prompt user convert the users input to float
    bookH = input prompt user convert the users input to float
    noOfbooks = input prompt users input 
    temp1 = bigBoxH // bookH  Calculate the no of books that can fit each big box
    noOfBigBox = noOfBooks // Calculate get total number of big boxes with books
    temp2 = smallBoxH // bookH  Calculate the remaining number of books that can fit small box
    noOfSmallBox = noOfBooks // temp1 Calculate number of small box
    if noOfBigBox is 0 and noOfSmallBox is 0
    print ship 1 small or ship 1 bib box
    return
    remBooks = noOfBooks % temp1 calculate remaining books
    noOfSmallBox = (remBooks // temp2) Calculate number of small box
    if (remBooks%smallBoxH) less than 0
    Incerement the noOfSmallBox by 1
    print ship small box number or ship big box number
    """
