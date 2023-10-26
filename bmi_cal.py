weight=float(input("Enter you weight in kilograms :- "))
height=float(input("Enter you height in meters:- "))
def bmi():
    a=height*height
    formula=(weight/a)
    roundof=round(formula,2)
    print("Your BMI is: ",roundof)

    if roundof<18.5:
        print("You are Underweight")
    elif roundof>= 18.5 and roundof<=24.9:
        print("Your weight is Normal. It means your Healthy!!!!!")
    elif roundof>=25.0  and roundof<=29.9:
        print("You are overweight")
    elif roundof>=30.0:
        print("You are Obese")

bmi()