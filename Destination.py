n = int(input("Enter number of destinations: "))

destinations = []

for i in range(n):
    destination = input("Enter destination: ")
    activities = input("Enter activities: ")

    destinations.append([destination, activities])

    print("\nComplete Itinerary:")
for destination, activities in destinations:
    print(destination, "-", activities)

    d = input("\nEnter destination: ")

for destination, activities in destinations:
    if destination.lower() == d.lower():
        print("Activities:", activities)

destination = input("\nEnter new destination: ")
activities = input("Enter activities: ")

destinations.append([destination, activities])

print("Destination added!")

d = input("\nEnter destination to remove: ")

for item in destinations:
    if item[0].lower() == d.lower():
        destinations.remove(item)
        print("Destination removed!")
        break

destinations.sort(key=lambda x: x[0]) 
search = input("Enter destination to search: ")

for day, destination, activities in destinations:
    if destination.lower() == search.lower():
        print(day, destination, activities)