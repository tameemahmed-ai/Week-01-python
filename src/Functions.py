def final_bill():
    food =float(input("enter food price: "))
    drinks = float(input("enter drinks price: "))
    dessert = float(input("enter dessert price: "))
    total = food + drinks + dessert
    tax = total * 0.1
    final = total + tax 
    print(f"Your total bill before tax: {total}")
    print(f"tax(10%): {tax}")
    print(f"Total bill: {final}")
final_bill()
    
    