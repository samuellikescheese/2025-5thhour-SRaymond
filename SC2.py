#Name:
#Class: 5th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be given a number as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

#Code Here:
print ("put in you weight(KG) and height(M)")
w = int(input())
h = int(input())
bmi = w / (h ** 2)
print(f"your BMI number is{bmi}")
if bmi < 18.5:
    print ("you are underweight")
elif 18.5 < bmi < 24.9:
    print ("you are normal weight")
elif 25 < bmi < 29.9:
    print ("you are overweight")
else:
    print ("you are obese")