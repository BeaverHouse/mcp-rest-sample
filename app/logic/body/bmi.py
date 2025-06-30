from models.body import BodyInfo

def check_obesity(info: BodyInfo) -> str:
    bmi = info.weight / ((info.height / 100) ** 2)
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"
