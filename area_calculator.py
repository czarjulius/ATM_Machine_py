import math  
status = True

while status:
    action = input("""
                Which shape do you wish to get the area?
                TRIANGLE
                CIRCLE
                ELLIPSE
                RECTANGLE
                TRAPEZIUM
                """)

    answer = action.upper()

    if answer == "TRIANGLE":    
        hieght =  int(input("Please Enter the hieght "))
        base =  int(input("Please Enter the base "))
        area_triangle = hieght * base * 0.5
        print("The area of the triangle is ", area_triangle)
        follow_up = print("Do You want to perform another transaction Yes(y)/ No(n)")
        trigger_status = input("Enter response ")
        trigger_status = trigger_status.upper()

        if trigger_status == 'N':
            status = False

    elif answer == "CIRCLE":
        radius =  float(input("Please Enter the radius "))
        area_circle = math.pi * (radius * radius)
        print("The area of the Circle is ", round(area_circle, 2))
        follow_up = print("Do You want to perform another transaction Yes(y)/ No(n)")
        trigger_status = input("Enter response ")
        trigger_status = trigger_status.upper()

        if trigger_status == 'N':
            status = False


    # Ellipse Area = πab
    elif answer == "ELLIPSE":
        major_axis =  int(input("Enter the major axis length "))
        minor_axis =  int(input("Enter the minor axis length "))
        area_ellice = math.pi * major_axis * minor_axis
        print("The area of the Ellipse is ", area_ellice)
        follow_up = print("Do You want to perform another transaction Yes(y)/ No(n)")
        trigger_status = input("Enter response ")
        trigger_status = trigger_status.upper()

        if trigger_status == 'N':
            status = False

    # Rectangle Area = w × h
    elif answer == "RECTANGLE":
        width =  int(input("Enter the length of the width "))
        hieght =  int(input("Enter the lenght of the height "))
        area_rectangle = width * hieght
        print("The area of the Ellipse is ", area_rectangle)
        follow_up = print("Do You want to perform another transaction Yes(y)/ No(n)")
        trigger_status = input("Enter response ")
        trigger_status = trigger_status.upper()

        if trigger_status == 'N':
            status = False

    # Trapezium (UK) Area = ½(a+b) × h     h = vertical height
    elif answer == "TRAPEZIUM":
        base_one =  int(input("Enter the length of base one "))
        base_two =  int(input("Enter the lenght of base two "))
        height =  int(input("Enter the height "))
        sum_base = base_one + base_two
        area_trapezium = (0.5 * sum_base) * height
        print("The area of the Trapezium is ", round(area_trapezium, 2))
        follow_up = print("Do You want to perform another transaction Yes(y)/ No(n)")
        trigger_status = input("Enter response ")
        trigger_status = trigger_status.upper()

        if trigger_status == 'N':
            status = False

    else:
        print("The option must be [TRIANGLE, CIRCLE, ELLIPSE, RECTANGLE, TRAPEZIUM]")