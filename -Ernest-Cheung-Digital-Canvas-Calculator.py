#Hi! Welcome to my Digital Canvas Calculator! For anyone that does Digital Painting this is self explanatory, but for those who don't heres the rundown on the purpose of this calculator!
#Basically, it changes the measurement unit of your canvas without actually changing how big the canvas this. The way is does that is by using the DPI to change from inches to pixel and pixels to inches.
print("Welcome to the Digital Canvas Calculator!")
intro = input("What is your name?")


welcome = f"Welcome back, {intro}"
print(welcome)

#Below, the DPI of your canvas is asked in order to calculate it in a later step. The DPI is the Dots Per Inch, which is how many pixels are in each inch. You can think of it as the resolution.
what_DPI = int(input(f"What DPI will your canvas be in?"))

print(what_DPI)

#The purpose for variable "inch_or_pixel" is to ask whether not the user would like to convert from inches to pixel or pixel to inches. 
inch_or_pixel = int(input("Would you like to change from inches to pixel or pixel to inches? If pixels to inches, type 1. If inches to pixel, type 2."))

#In the following, I used conditional statements to differetiate two options above. 

if (inch_or_pixel == 1): 
    pixel_to_inches = str(input("How many pixels are one length of your canvas?"))
    print(pixel_to_inches)
    pixel_to_inches_answer = float(pixel_to_inches) / what_DPI
    print(f"{pixel_to_inches} pixels turn into {pixel_to_inches_answer} inches")
#Above, this is choice 1, which is to convert from pixel to inches. I first ask how many pixels are on one of the lengths. Then, I divided the stated pixel number with the stated DPI to get the inches of the stated pixels.



#Below, this is choice 2, which is to convert from inches to pixel. I first ask how many inches are on one of the lengths. Then, I multiplied the stated inches with the state DPI to get the pixels of the stated inches.
if (inch_or_pixel == 2):
    inches_to_pixel = str(input("How many inches is one side of your canvas?"))
    print(inches_to_pixel)
    inches_to_pixel_answer = float(inches_to_pixel) * what_DPI
    print(f"{inches_to_pixel} inches turn into {inches_to_pixel_answer} pixels")


#The use for this calculation is to know what measurements to have when changing units in a digital canvas environment. It makes it faster and easier to convert units efficiently.






