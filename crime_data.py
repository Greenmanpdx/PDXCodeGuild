import csv
import operator
from collections import Counter

# class crime_data:



def open_file(file_to_open):
    with open(file_to_open, 'r') as data_sheet:
        # read_data = csv.DictReader(data_sheet)

        read_data = csv.reader(data_sheet, delimiter=',', )
        headers = read_data.__next__()
        data_dict = {}
        for h in headers:
            data_dict[h] = []

        for row in read_data:
            for h, v in zip(headers, row):
                data_dict[h].append(v)

        row_count = len(data_dict['Major Offense Type'])
        return data_dict, row_count






#Main starts here
file_2011 = 'crime_incident_data_2011.csv'
file_2012 = 'crime_incident_data_2012.csv'
file_2013 = 'crime_incident_data_2013.csv'
file_2014 = 'crime_incident_data_2014.csv'
file_recent = 'crime_incident_data_recent.csv'

data_dict_2011 = {}
data_dict_2011, count_2011 = open_file(file_2011)
data_dict_2012 = {}
data_dict_2012, count_2012 = open_file(file_2012)
data_dict_2013 = {}
data_dict_2013, count_2013 = open_file(file_2013)
data_dict_2014 = {}
data_dict_2014, count_2014 = open_file(file_2014)


combined = data_dict_2011.copy()
combined.update(data_dict_2012)
combined.update(data_dict_2013)
combined.update(data_dict_2014)


stats = {'2011' : count_2011, '2012' : count_2012, '2013' : count_2013, '2014' : count_2014}


most_crimes = Counter(combined['Major Offense Type']).most_common()[0]
least_crimes = Counter(combined['Major Offense Type']).most_common()[-1]
highest_year = Counter()
print(most_crimes)
print(least_crimes)
maximum = max(stats, key=stats.get)  # Just use 'min' instead of 'max' for minimum.
print(maximum, stats[maximum])




