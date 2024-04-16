def name_country(podstawowy):
    with open(podstawowy, 'r') as plik:
        first_line = plik.readline().strip()
        countries = first_line.split(',')
        print(countries)
        print("Wybierz numer kraju:")
        for country in countries:
            print(country.strip())
def choose_country(podstawowy, number):
    with open(podstawowy, 'r') as plik:
        first_line = plik.readline().strip()
        countries = first_line.split(',')
        for country_info in countries:
            if country_info.startswith(number):
                country = country_info[len(number):].strip()
                print("Wybrano kraj:", country)
                return country
    print("Kraj o podanym numerze nie istnieje.")
    return None
