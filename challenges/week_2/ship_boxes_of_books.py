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
if name=="main":
    main()
