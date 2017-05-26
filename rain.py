"""Make it rain"""
import operator
import urllib.request
from bs4 import BeautifulSoup

def read_in_file(file):

    f = open(file, 'r')
    unformatted_file = f.readlines()

    return unformatted_file


def make_table(file):

    table = [line.split() for line in file]

    return table

def strip_headers(unformatted_table):

    while unformatted_table[0] != ['------------------------------------------------------------------------------------------------------------------']:
        unformatted_table.pop(0)
    unformatted_table.pop(0)
    for L in unformatted_table:
        if '<' in L[0]:
            L.pop(0)
            # L[0].remove('</p>')
            # L.remove('</body>')
            # L.remove('</html>')
    print(unformatted_table)

    return unformatted_table

def remove_hours(headless_table):
    return [L[:2] for L in headless_table]


def convert_rain_to_int(table):
    """

    # >>> convert_rain_to_int(['1', '2'])
    # ['1', 2]
    #
    # :param table:
    # :return: void
    # """
    for L in table:
        if L[1] == '-':
            L[1] = 0
        L[1] = int(L[1])


def find_highest_day(table):
    """

    # >>> find_highest_day([['Mar', 1],['Feb', 2]])
    # 'Feb'
    #
    # :param table:
    # :return:
    # """
    convert_rain_to_int(table)
    highest_rain = 0
    for L in table:
        if L[1] > highest_rain:
            highest_rain = L[1]
            highest_day = 'The highest day was ' + str(L[0]) + ' with ' + str(L[1]) + ' inches.'

    return highest_day


def seperate_year(table):
    year_table = [[table[x][y] for y in range(len(table[0]))] for x in range(len(table))]
    for L in year_table:
        L[0] = int((L[0].split('-'))[2])
    return year_table





def find_highest_year(table):
    year = 2016
    year_table = []
    running_total = 0
    for L in table:
        if L[0] == year:
            running_total += L[1]

        else:
            year_table.append([year, running_total])
            year = L[0]
            running_total = L[1]
    highest_year = 0
    for line in year_table:
        if line[1] > highest_year:
            highest_year = line[1]
            highest_year_string = ' ' + str(line[0]) + ' with ' + str(line[1])
    return highest_year_string


def seperate_date(table):
    for L in table:
        L.insert(1, L[0].split('-'))
        L.remove(L[0])


def create_average_day_dict(table):

    # date = []
    data_by_date = {}
    #print(table)

    for L in table:
        if (L[0][0], L[0][1]) in data_by_date:
            data_by_date[L[0][0], L[0][1]] += L[1]
        else:
            data_by_date[L[0][0], L[0][1]] = L[1]

    return data_by_date


def find_highest_average_day(data_by_date):
    highest_date = max(data_by_date, key=data_by_date.get)
    return highest_date


def esitmate_rain_by_date(data_by_day, date_to_test):
    """

    # >>> esitmate_rain_by_date(data_by_day)
    #
    # :param data_by_day:
    # :return:
    # """

    average_rain_by_date = data_by_day[date_to_test]/12
    #print(average_rain_by_date)
    return average_rain_by_date


def input_date():
    month_to_test = input('Enter the month ie JAN, FEB \n')
    day_to_test = input('Enter the day dd with leading 0s\n')
    date_to_test = (day_to_test, month_to_test)
    print(date_to_test)
    return date_to_test


def output_answer(day, year,  highest_average_day, estimation_for_date):

    print('The highest rainfall was on ' + day)
    print('The highest year for rainfall was' + year)
    print('The highest average rainfall per day is ' + str(highest_average_day))
    print('It is estimated that the rainfall on your selected day will be ' + str(estimation_for_date) + 'inches')


def menu_display():
    quit = False
    while quit != True:
        print("""
        The Rain Whisper: Everything you didn't want to know about Portland rain.
        Select Region
        1. North Region
        # 2. NW Region
        # 3. NE Region
        # 4. SW Region
        # 5. SE Region
        # 6. Other
        7. Quit
        """)

        answer = int(input())

        quit = region(answer)


def region(answer):

    if answer == 1:
        quit = north_region()
    # elif answer == 2:
    #     quit = nw_region()
    # elif answer == 3:
    #     quit = ne_region()
    # elif answer == 4:
    #     quit =  sw_region()
    # elif answer == 5:
    #     quit = se_region()
    # elif answer == 6:
    #     quit = other()
    elif answer == 7:
        quit = True
    else:
        print('Invalid entry, try again')
        quit = False
    return quit


def north_region():
    print("""
    Select a Rain Gage
    1. Hayden Island Rain Gage
    2. Open Meadows School Rain Gage
    3. Shipyard Rain Gage
    4. Columbia IPS Rain Gage
    5. Albina Rain Gage
    6. Swan Island Rain Gage 122
    7. Marine Drive Rain Gage
    8. Simmons Rain Gage
    9. Cascade PCC Rain Gage
    10. WPCL Rain Gage
    11. Terminal 4 NE Rain Gage
    12. Astor Elementary School Rain Gage
    13. Swan Island Rain Gage
    14. Change Regions
    15. Quit
    """)
    answer = 0
    answer = int(input())
    quit = False
    while quit != True:
        if answer == 1:
            quit = load_url_file('http://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
        elif answer == 2:
            quit = load_url_file('http://or.water.usgs.gov/non-usgs/bes/open_meadows.rain')
        elif answer == 3:
            quit = load_url_file('http://or.water.usgs.gov/non-usgs/bes/shipyard.rain')
        elif answer == 4:
            quit = load_url_file('http://or.water.usgs.gov/non-usgs/bes/columbia_ips.rain')
        elif answer == 5:
            quit = load_url_file('http://or.water.usgs.gov/non-usgs/bes/albina.rain')
        elif answer == 6:
            quit = load_url_file('http://or.water.usgs.gov/non-usgs/bes/swan_island.rain')
        elif answer == 7:
            quit = load_url_file('http://or.water.usgs.gov/non-usgs/bes/marine_drive.rain')
        elif answer == 8:
            quit = load_url_file('http://or.water.usgs.gov/non-usgs/bes/simmons.rain')
        elif answer == 9:
            quit = load_url_file('http://or.water.usgs.gov/non-usgs/bes/pcc_cascade.rain')
        elif answer == 10:
            quit = load_url_file('http://or.water.usgs.gov/non-usgs/bes/wpcl.rain')
        elif answer == 11:
            quit = load_url_file('http://or.water.usgs.gov/non-usgs/bes/terminal4ne.rain')
        elif answer ==12:
            load_url_file('http://or.water.usgs.gov/non-usgs/bes/astor.rain')
        elif answer == 13:
            quit = load_url_file('http://or.water.usgs.gov/non-usgs/bes/swan_island_pump.rain')
        elif answer == 14:
            return False
        elif answer == 15:
            return True
        else:
            print('Invalid entry, try again')
        return quit



def load_url_file(link):
    r = urllib.request.urlopen(link)
    soup = BeautifulSoup(r, "lxml")
    text = soup.getText()

    f = open('rain.txt', 'w')
    f.write(text)
    quit = run_data('rain.txt')

    return quit


def run_data(file):
    unformatted_file = read_in_file(file)
    unformatted_table = make_table(unformatted_file)
    headerless_table = strip_headers(unformatted_table)
    daily_table = remove_hours(headerless_table)


    highest_day = find_highest_day(daily_table)
    year_table = seperate_year(daily_table)
    highest_year = find_highest_year(year_table)
    seperate_date(daily_table)
    data_by_day = create_average_day_dict(daily_table)
    highest_average_day = find_highest_average_day(data_by_day)
    # print(data_by_day)
    date_to_test = input_date()
    estimation_for_date = esitmate_rain_by_date(data_by_day, date_to_test)
    output_answer(highest_day, highest_year, highest_average_day, estimation_for_date)

    select = input('Would you like to view another?')

    if select == 'y' or select == 'Y':
        return False
    elif select == 'n' or select == 'N':
        return True
    else:
        print('Invalid entry. exiting')
        return True

def main():
    menu_display()



main()