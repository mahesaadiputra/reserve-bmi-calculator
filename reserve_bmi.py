






def main():
    print("======Reserve BMI Calculator========")
    print("============= By Mahesa ============")
    print()
    height = float(input("Input your Height (cm) :"))
    bmi = float(input("Input your BMI:"))
    inc_height = height / 2.54
    weight = bmi * (inc_height ** 2) /703
    kg =  weight / 2.2046    
    round_kg = "{:.2f}".format(kg)
    print()
    print(f"In order to achieve a BMI of {bmi} you need to weigh {round_kg} kilograms (kg)")
    


main()