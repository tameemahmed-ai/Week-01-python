def wash_clothes(temperature, spin_speed):
    print(f"Washing at {temperature} degrees")
    print(f"Spin speed: {spin_speed}")
    print("Done!")

# collect input outside the function
temperature = input("Enter washing temperature: ")
spin_speed = input("Enter spin speed (slow/fast/gentle): ")

# pass it into the function
wash_clothes(temperature, spin_speed)
10