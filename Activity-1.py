# Custom Ride Builder


print("====================================")
print("      Welcome to Ride Builder!      ")
print("====================================")
print()

print("Step 1: Pick your vehicle")
print("  1 - Bicycle")
print("  2 - Bike")
print()

choice = int(input("Enter 1 or 2: "))
print()

if choice == 1:
    # Nested if-else — runs only when choice is 1
    print("Step 2: Pick your cycle type")
    print("  1 - Hybrid Bike")
    print("  2 - Gravel Bike")
    print()

    cycle_type = int(input("Enter 1 or 2: "))
    print()

    if cycle_type == 1:
        print("You picked  : Hybrid Bike")
        print("Top speed   : 35 km/h")
        print("Best for    : Casual rides")
    else:
        print("You picked  : Gravel Bike")
        print("Top speed   : 45 km/h")
        print("Best for    : Long distance adventure")

elif choice == 2:
    # Nested if-else — runs only when choice is 2
    print("Step 2: Pick your bike type")
    print("  1 - Commuter")
    print("  2 - Super Bike")
    print()

    bike_type = int(input("Enter 1 or 2: "))
    print()

    if bike_type == 1:
        print("You picked  : Commuter")
        print("Top Speed   : 80 km/h")
        print("Best for    : Daily city traffic")
    else:
        print("You picked  : Super Bike")
        print("Top Speed   : 140 km/hr")
        print("Best for    : Highway cruising")

else:
    print("That was not a valid choice.")
    print("Please enter 1 for Cycle or 2 for Bike.")

print()
print("====================================")
print("   Your custom ride is ready!       ")
print("   Enjoy the journey!               ")
print("====================================")
