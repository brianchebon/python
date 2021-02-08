def shipping_boxes():
    big_box = float(input("Enter the height of the big box in inches: "))
    small_box = float(input("Enter the height of the small box in inches: "))
    book_thickness = float(input("Enter the thickness of 1 book in inches: "))
    no_of_books = int(input("Enter the no of books to be shipped: "))
    # get the height of the books in total
    height_of_books = book_thickness*no_of_books
    # check how many big boxes are required first
    if height_of_books > big_box:
        # get the number of big boxes first
        no_of_big_boxes = height_of_books//big_box
        remaining_books = height_of_books % big_box
        # check if remaining books is greater than the small box to know how many small boxes will be required
        if remaining_books > small_box:
            if remaining_books % small_box > 0:
                no_of_small_boxes = (remaining_books//small_box) + 1
                print("Ship {} large boxes and {} small boxes".format(
                    no_of_big_boxes, no_of_small_boxes))
            else:
                no_of_small_boxes = remaining_books//small_box
                print("Ship {} large boxes and {} small boxes".format(
                    no_of_big_boxes, no_of_small_boxes))
        # check if there are no remaining books to ship only big boxes
        elif remaining_books == 0:
            print("Ship {} large boxes".format(no_of_big_boxes))
        #i f remaining books is not greater than the size of small box place the remaining books into one small box
        else:
            no_of_small_boxes = 1
            print("Ship {} large boxes and {} small box".format(
                no_of_big_boxes, no_of_small_boxes))
    # check if the books height is equal to the height of one big box to return one big box
    elif height_of_books == big_box:
        no_of_big_boxes =1
        print("Ship {} big box or Ship {} big box".format(no_of_big_boxes, no_of_big_boxes))
    # check if height of books is greater than the small box size and if there is a remainder in the books to fill the small boxes
    elif height_of_books > small_box and height_of_books % small_box > 0:
        no_of_small_boxes = (height_of_books//small_box) + 1
        print("ship {} small boxes".format(no_of_small_boxes))
    # check if the height of books is greater than the small box but no remaining books
    elif height_of_books > small_box and height_of_books % small_box == 0:
        no_of_small_boxes = height_of_books/small_box
        print("ship {} small boxes".format(no_of_small_boxes))
    # check if the height of books is less than a small box to ship them in one small box
    elif height_of_books <= small_box:
        print("Ship 1 small box or ship 1 big box")


if __name__ == '__main__':
    shipping_boxes()
