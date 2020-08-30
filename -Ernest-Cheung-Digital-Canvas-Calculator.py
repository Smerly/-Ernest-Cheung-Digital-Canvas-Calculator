print("Welcome to the Digital Canvas Calculator!")
intro = input("What is your name?")


welcome = f"Welcome back, {intro}"
print(welcome)

what_DPI = int(input(f"What DPI will your canvas be in?"))

print(what_DPI)


inch_or_pixel = int(input("Would you like to change from inches to pixel or pixel to inches? If pixels to inches, type 1. If inches to pixel, type 2."))

if (inch_or_pixel == 1): 
    pixel_to_inches = str(input("How many pixels are one length of your canvas?"))
    print(pixel_to_inches)
    pixel_to_inches_answer = float(pixel_to_inches) / what_DPI
    print(f"{pixel_to_inches} pixels turn into {pixel_to_inches_answer} inches")


if (inch_or_pixel == 2):
    inches_to_pixel = str(input("How many inches is one side of your canvas?"))
    print(inches_to_pixel)
    inches_to_pixel_answer = float(inches_to_pixel) * what_DPI
    print(f"{inches_to_pixel} inches turn into {inches_to_pixel_answer} pixels")






