print("E22CSEU1134")
print("Vaibhav Uttamchandani")


flight_data = [
    {"Flight ID": "AI161E90", "From": "BLR", "To": "BOM", "Price": 5600},
    {"Flight ID": "BR161F91", "From": "BOM", "To": "BBI", "Price": 6750},
    {"Flight ID": "AI161F99", "From": "BBI", "To": "BLR", "Price": 8210},
    {"Flight ID": "VS171E20", "From": "JLR", "To": "BBI", "Price": 5500},
    {"Flight ID": "AS171G30", "From": "HYD", "To": "JLR", "Price": 4400},
    {"Flight ID": "AI131F49", "From": "HYD", "To": "BOM", "Price": 3499}
]

city_codes = {
    "BLR": "Bengaluru",
    "BOM": "Mumbai",
    "BBI": "Bhubaneswar",
    "HYD": "Hyderabad",
    "JLR": "Jabalpur"
}

def search_flights_by_city(city):
    city_flights = []
    for flight in flight_data:
        if flight["From"] == city or flight["To"] == city:
            city_flights.append(flight)
    return city_flights

def search_flights_from_city(city):
    from_city_flights = []
    for flight in flight_data:
        if flight["From"] == city:
            from_city_flights.append(flight)
    return from_city_flights

def search_flights_between_cities(city1, city2):
    between_cities_flights = []
    for flight in flight_data:
        if (flight["From"] == city1 and flight["To"] == city2) or (flight["From"] == city2 and flight["To"] == city1):
            between_cities_flights.append(flight)
    return between_cities_flights

while True:
    print("Search Options:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        city = input("Enter the city code: ").upper()
        if city in city_codes:
            flights = search_flights_by_city(city)
            if flights:
                print(f"Flights for {city_codes[city]}:")
                for flight in flights:
                    print(f"Flight ID: {flight['Flight ID']}, To: {city_codes[flight['To']]}, Price: {flight['Price']}")
            else:
                print("No flights found for the specified city.")
        else:
            print("Invalid city code.")
    
    elif choice == "2":
        city = input("Enter the city code: ").upper()
        if city in city_codes:
            flights = search_flights_from_city(city)
            if flights:
                print(f"Flights from {city_codes[city]}:")
                for flight in flights:
                    print(f"Flight ID: {flight['Flight ID']}, To: {city_codes[flight['To']]}, Price: {flight['Price']}")
            else:
                print("No flights found from the specified city.")
        else:
            print("Invalid city code.")

    elif choice == "3":
        city1 = input("Enter the first city code: ").upper()
        city2 = input("Enter the second city code: ").upper()
        if city1 in city_codes and city2 in city_codes:
            flights = search_flights_between_cities(city1, city2)
            if flights:
                print(f"Flights between {city_codes[city1]} and {city_codes[city2]}:")
                for flight in flights:
                    print(f"Flight ID: {flight['Flight ID']}, To: {city_codes[flight['To']]}, Price: {flight['Price']}")
            else:
                print("No flights found between the specified cities.")
        else:
            print("Invalid city code(s).")

    elif choice == "4":
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")

