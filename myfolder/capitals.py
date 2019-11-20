'''This is a dictionary

that list all the State of EU linked to respective Capital City.
'''

list_of_capitals = {'Aland Islands': 'Mariehamn',
                    'Albania': 'Tirana',
                    'Andorra': 'Andorra la Vella',
                    'Armenia': 'Yerevan',
                    'Austria': 'Vienna',
                    'Azerbaijan': 'Baku',
                    'Belarus': 'Minsk',
                    'Belgium': 'Brussels',
                    'Bosnia and Herzegovina': 'Sarajevo',
                    'Bulgaria': 'Sofia',
                    'Croatia': 'Zagreb',
                    'Cyprus': 'Nicosia',
                    'Czech Republic': 'Prague',
                    'Denmark': 'Copenhagen',
                    'Estonia': 'Tallinn',
                    'Faroe Islands': 'Torshavn',
                    'Finland': 'Helsinki',
                    'France': 'Paris',
                    'Georgia': 'Tbilisi',
                    'Germany': 'Berlin',
                    'Gibraltar': 'Gibraltar',
                    'Greece': 'Athens',
                    'Guernsey': 'Saint Peter Port',
                    'Hungary': 'Budapest',
                    'Iceland': 'Reykjavik',
                    'Ireland': 'Dublin',
                    'Isle of Man': 'Douglas',
                    'Italy': 'Rome',
                    'Jersey': 'Saint Helier',
                    'Kosovo': 'Pristina',
                    'Latvia': 'Riga',
                    'Liechtenstein': 'Vaduz',
                    'Lithuania': 'Vilnius',
                    'Luxembourg': 'Luxembourg',
                    'Macedonia': 'Skopje',
                    'Malta': 'Valletta',
                    'Moldova': 'Chisinau',
                    'Monaco': 'Monaco',
                    'Montenegro': 'Podgorica',
                    'Netherlands': 'Amsterdam',
                    'Northern Cyprus': 'North Nicosia',
                    'Norway': 'Oslo',
                    'Poland': 'Warsaw',
                    'Portugal': 'Lisbon',
                    'Romania': 'Bucharest',
                    'Russia': 'Moscow',
                    'San Marino': 'San Marino',
                    'Serbia': 'Belgrade',
                    'Slovakia': 'Bratislava',
                    'Slovenia': 'Ljubljana',
                    'Spain': 'Madrid',
                    'Svalbard': 'Longyearbyen',
                    'Sweden': 'Stockholm',
                    'Switzerland': 'Bern',
                    'Turkey': 'Ankara',
                    'Ukraine': 'Kyiv',
                    'United Kingdom': 'London',
                    'Vatican City': 'Vatican City'}


'''The first function check_capital control if,

given a name of a country, this country is an European state.
'''


def check_capital(state_name):

    if state_name in list_of_capitals:
        print("The capital of {} is {}".
              format(state_name, list_of_capitals[state_name]))
    else:
        print("Sorry, {} does not seem to be an European state".
              format(state_name))


'''The second function capital_name,

given a name of a capital,

it returns the name of the country whose capitalis equal to the input.
'''


def check_state(capital_name):

    for state, capital in list_of_capitals.items():
        if capital == capital_name:
            print("The European state whose capital is {} is {}".
                  format(capital_name, state))
            return

    print("Sorry, {} is not the capital of any European state".
          format(capital_name))
