# estate.py

"""
Title: Real Estate Data Handling
Author: Alice Cai
Date: 2026-02-03
"""

"""
Lab Description:

Option 1: Location Based Property Report Generator

Uses the data files properties.txt, ownership.txt, price_index.txt to calculate average area, average price, and number of available properties. Prints the results out in a nice table. 
"""

"""
File Information:

properties.txt: a list of property records. 
<location,number of rooms,area,owner ID>
- owner ID is number from 0-6
- 0 is no owner
- 1-5 is index value of firms in ownership.txt
- 6 is privately owned

ownership.txt: information about firms in property market. 
<owner ID,name of firm,year of establishment>

price_index.txt: average price of square foot per locality
<locality,average price>
"""

# planning
"""
average area per locality: 

location in price_index.txt --> find all the listings in properties.txt that match that location --> find the area of the listing (index = 2) --> take all the areas and average them --> print out the average in the table
- properties has many properties with the same location: if using location as key, the value should be a list with the rest of the information
- if using lists, iterate through lists to create new list

average price per locality:

average area per locality * average price per square feet in that locality --> print out in table

number of available properties:

count the total number of properties with ID 0 listed in properties.txt per locality
- if using dictionary could be len(value)
- if using lists iterate through list

Conclusion: let's use dictionary
"""

def load_data(filename):
    """
    Gets the file data.
    :param filename: name of the file (str)
    :return: data (list)
    """

    # open file
    with open(filename, "r") as file:
        data = file.readlines()

    # process list
    data.pop(0)  # remove header
    for i in range(len(data)):
        data[i] = data[i].strip()
        data[i] = data[i].split(",")
        for j in range(1, len(data[i])):  # skip str name
            data[i][j] = float(data[i][j])

    return data

def build_dictionary(price_index, properties):
    """
    Makes a dictionary of base info from the file list
    :param price_index: A list with the price index file information (list)
    :param properties: A list with the properties file information (list)
    :return: property_dict (dict)
    """

    property_dict = {}
    # populate dictionary with locations
    for i in range(len(price_index)):
        property_dict[price_index[i][0]] = [[price_index[i][1]]]

    # populate locations with properties
    for key in property_dict.keys():
        for i in range(len(properties)):
            if key == properties[i][0]:
                property_dict[key].append(properties[i][1:])

    return property_dict

def average_area(property_dict):
    """
    Adds average area information into a new dictionary for processed information.
    :param property_dict: (dict)
    :return: average_area_dict (dict)
    """

    # dictionary for processed information
    average_area_dict = {}

    # populate with location and average area
    for key, value in property_dict.items():
        sum = 0
        for i in range(1, len(value)):
            sum += value[i][1]
        average_area_dict[key] = [(sum/(len(value)-1))]

    return average_area_dict

def average_price(average_dict, property_dict):
    """
    Populates the dictionary with average price
    :param average_dict: (dict)
    :param property_dict: (dict)
    :return: average_dict (dict)
    """

    # append average price information
    for key in average_dict.keys():
        average_dict[key].append(average_dict[key][0] * property_dict[key][0][0])

    return average_dict

def get_available_properties(average_dict, property_dict):
    """
    Counts the number of available properties per location
    :param average_dict: (dict)
    :param property_dict: (dict)
    :return: average_dict (dict)
    """

    # for each location count available properties
    for key in average_dict.keys():
        count = 0
        for i in range(1, len(property_dict[key])):
            if int(property_dict[key][i][2]) == 0:
                count += 1
        average_dict[key].append(count)

    return average_dict

def sort_table(average_dict):
    """
    Sorts the dictionary
    :param average_dict: (dict)
    :return: average_dict (list)
    """

    # sort the dictionary (into list)
    average_dict = sorted(average_dict.items(), key=lambda x: (-x[1][2], x[0]))

    return average_dict


def print_table(average_dict):
    """
    Prints the table of information out.
    :param average_dict: (dict)
    :return: None
    """

    # print table
    # header
    print(f"+{'':-<15}+{'':-<15}+{'':-<15}+{'':-<11}+")
    print(f"| {'Location':<13} |{'Average Area':^15}| {'Average Price':>12} | {'Available':>8} |")
    print(f"+{'':-<15}+{'':-<15}+{'':-<15}+{'':-<11}+")

    # print table
    for i in range(len(average_dict)):
        print(f"| {average_dict[i][0]:<13} |{average_dict[i][1][0]:^10,.2f}sqft | {'$ '}{average_dict[i][1][1]:>11,.2f} | {average_dict[i][1][2]:>9} |")

    print(f"+{'':-<15}+{'':-<15}+{'':-<15}+{'':-<11}+")

def main():
    price_index = load_data("price_index.txt")
    properties = load_data("properties.txt")
    property_dict = build_dictionary(price_index, properties)
    average_dict = average_area(property_dict)
    average_dict = average_price(average_dict, property_dict)
    average_dict = get_available_properties(average_dict, property_dict)
    average_dict = sort_table(average_dict)
    print_table(average_dict)

if __name__ == "__main__":
    main()