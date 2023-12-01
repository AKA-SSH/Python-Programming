def BMI(w, h):
    BMI= w/h**2
    if BMI < 18.5:
        return 'underweight'
    elif 18.5 <= BMI <= 24.9:
        return 'normal'
    elif 25 <= BMI <= 29.9:
        return 'overweight'
    else:
        return 'obese'
print(BMI(85, 1.77))