weight = 57
height = 1.73

def calculate_bmi(height, weight): 
    print("Height = " + str(height)) 
    print("Weight = " + str(weight))
    
#Add code here to calculate BMI 
BMI = (weight)/(height**2)

#Add code here to display calculate BMI
print("Your BMI is " + str(BMI))

calculate_bmi(weight=57, height=1.73)

if BMI < 18.5:
    print("Under Weight")
elif 18.5 <= BMI <= 25.0:
    print("Normal Weight")
else:
    print("Over Weight")

