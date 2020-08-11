
radius = float(input("Enter the radius: "))


area=3.141*radius*radius


print("Area of the circle is", area, "sq units")


filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
