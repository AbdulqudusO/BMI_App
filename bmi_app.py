w=input("What is your weight\n")
w=float(w)
h=input("What is your height in meters\n")
h=float(h)

def BMI_calc(w,h):
    BMI=(w/(h**2))
    BMI=round(BMI,1)
    
    if BMI < 18.5:
        print (f"Your BMI is: {BMI}\nUnderweight")
    elif 18.4< BMI < 25:
        print (f"Your BMI is: {BMI}\nNormal")
    elif 24.9< BMI < 30:
        print (f"Your BMI is: {BMI}\nOverweight")
    elif 29.9< BMI <35:
        print (f"Your BMI is: {BMI}\nClass 1 Obesity")
    elif 34.9< BMI <40:
        print (f"Your BMI is: {BMI}\nClass 2 Obesity")
    else:
        print (f"Your BMI is: {BMI}\nExtreme Obesity")
        
BMI_calc(w,h)
