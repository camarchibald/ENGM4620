# main.py - Cameron Archibald and Nader Hdeib, 21-02-2025
# Main program loop

import scrape
from scrape import CityData
import plot

import pickle


# Print all cities that have data
def print_cities(data: list[CityData]):
    if data:
        for i, city in enumerate(data):
            print("Position: ", i, " Name: ", city.city_name, " Houses: ", len(city.house_data))
    else:
        print("No data, try unpickling")


# Ask user to enter index, validate that it doesn't exceed amount of cities
def ask_and_validate_index(data: list[CityData]) -> int | None:
    print_cities(data)
    i = input("Choose a city by index (q to go back): ")
    if i.isnumeric():
        i = int(i)
        if i < len(data):
            return i
        else:
            print("Invalid index")
            return None
    else:
        return None


# Main control loop
def main():
    data = []

    command = ''
    while command != 'q':
        command = input('\nEnter command: ')
        pass
        match command:
            # Scrape the data
            case 's':
                i = ask_and_validate_index(data)
                if i is not None:
                    data[i] = scrape.scrape(city=data[i], max_batch_size=10)

            # Pickle the data
            # TODO: Data will be overwritten if it isn't unpickled first
            case 'p':
                if data:
                    f = open('data', 'wb')
                    pickle.dump(data, f)
                    f.close()
                else:
                    print("No data")
                pass

            # Unpickle the data
            case 'u':
                f = open('data', 'rb')
                data = pickle.load(f)
                f.close()
                print_cities(data)
                pass

            # Create new city
            case 'n':
                name = input('Enter city name (q to go back): ')
                if name != "q":
                    data.append(CityData(name=name))
                pass

            # View data of one city
            case 'v':
                i = ask_and_validate_index(data)
                if i is not None:
                    data[i].print_data()
                pass

            # Create map
            case 'm':
                i = ask_and_validate_index(data)
                if i is not None:
                    plot.plot(data[i])
                pass


if __name__ == "__main__":
    main()
