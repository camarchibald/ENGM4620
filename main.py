# main.py - Cameron Archibald and Nader Hdeib, 21-02-2025
# Main program loop

import scrape
from scrape import CityData

import pickle


# TODO allow for different cities to be inputted
# Main control loop
def main():
    command = ''
    while command != 'q':
        command = input('Enter command: ')

        match command:
            # Scrape the data
            # TODO if halifax is not created or unpickled this fails
            case 's':
                halifax = scrape.scrape(city=halifax, max_batch_size=50)
                pass

            # Pickle the data
            # TODO if halifax is not created this fails
            case 'p':
                if halifax:
                    f = open('halifax', 'wb')
                    pickle.dump(halifax, f)
                    f.close()
                pass

            # Unpickle the data
            case 'u':
                f = open('halifax', 'rb')
                halifax = pickle.load(f)
                f.close()
                if halifax:
                    for house in halifax.house_data:
                        print(house)
                pass

if __name__ == "__main__":
    main()