import math  

action = input("Enter Action ")
answer = action.upper()

if answer == "TRIANGLE":    
    hieght =  int(input("Please Enter the hieght "))
    base =  int(input("Please Enter the base "))
    area_triangle = hieght * base * 0.5
    print("The area of the triangle is ", area_triangle)

elif answer == "CIRCLE":
    radius =  float(input("Please Enter the radius "))
    area_circle = math.pi * (radius * radius)
    print("The area of the Circle is ", round(area_circle, 2))


# (0°C × 9/5) + 32 = 32°F
elif answer == "CONVERT":
    value =  float(input("Please Enter the value to convert "))
    result = (value * (9/5) + 32)
    print("The area of the Circle is ", result)

else:
    print("The option must be [TRIANGLE, CIRCLE, CONVERT]")