def final_bill(food, drinks, dessert):
    # PROCESS
    total = food + drinks + dessert
    tax = total * 0.1
    final = total + tax

    # OUTPUT
    print(f"Your bill before tax: ${total}")
    print(f"Tax (10%): ${tax}")
    print(f"Total bill: ${final}")

try:
# INPUTS — collected outside the function
    food = float(input("Enter food price: "))
    drinks = float(input("Enter drinks price: "))
    dessert = float(input("Enter dessert price: "))
    final_bill(food, drinks, dessert)
# Call the function and pass values in

except ValueError:
    print("Please enter a valid number for food, drinks, and dessert prices.")
    

    