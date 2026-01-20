# Assignment 1

"""
Title: Assignment 1
Author: Alice Cai
Date: 2026-01-18
"""

"""
Apply all software quality requirements. 
Validation is required for all inputs.
- object type validation

break and continue is not allowed
no external modules are allowed
"""

"""
file information: (txt format)

country.txt: contains the trade information for all countries

    country code | country name | imports ($) | exports ($)

tariff.txt: contains tariffs imposed by your country on foreign industries

    country code | industry | percentage rate

product.txt: general info about each product

    product ID | industry | name

product_country.txt: which countries produce which products and at which price

    product ID | country code | price

shopping_list.txt: the list of PIDs Terra Nova Trading purchases

    Product ID
"""

"""
### --- SECTION A --- ###
Goal: Calculate the trade deficit for each foreign country and return the top five countries in descending order. 

Trade deficit can be calculated by import - export
"""

def load_file(filename):
    """
    input: filename (str)
    process: loads the file and places into nested list
    return: country_list (2D list)
    """
    ### --- Load Country File --- ###

    with open(filename, "r") as file:
        data = file.readlines()  # list

    if filename == "country.txt":
        # country does not have spaces between data
        # strip \n and split into list

        for i in range(len(data)):
            data[i] = data[i].strip()
            data[i] = data[i].split(",")

        # Place country data into list
        # [country code, country name, imports, exports]
        # also convert import and export to floats

        country_list = []

        for i in range(len(data)):
            if i != 0:  # exclude title row
                country_list.append([data[i][0], data[i][1], float(data[i][2]), float(data[i][3])])

        return country_list

    elif filename == "product.txt":

        # products have spaces in between data
        for i in range(len(data)):
            data[i] = data[i].strip()
            data[i] = data[i].split(", ")

        return data[1:]  # exclude title row

    elif filename == "product_country.txt":
        # product country has spaces in between data
        for i in range(len(data)):
            data[i] = data[i].strip()
            data[i] = data[i].split(", ")

        data = data[1:]
        for i in range(len(data)):
            data[i][2] = int(data[i][2])  # exclude title row
        return data


def find_trade_deficits(country_list):
    """
    input: country_list (list)
    process: adds an index to each sublist representing trade deficit
    return: country_list
    """

    # trade deficit = imports - exports
    for i in range(len(country_list)):
        country_list[i].append(country_list[i][2] - country_list[i][3])

    return country_list


def get_trade_deficits(country_list):
    """
    input: country_list (list)
    process: returns the trade deficit of a country
    return: country_list[4] (float)
    """
    return country_list[4]


def sort_deficits(country_list):
    """
    input: country_list (list)
    process: Sorts the list in descending order based on trade deficit
    return: country_list (list), sorted
    """

    # sort list by trade deficit
    country_list.sort(reverse=True, key=get_trade_deficits)

    return country_list


def show_deficits(country_list):
    """
    input: country_list (list)
    process: shows the countries with top 5 trade deficits in a nice table
    return: none
    """

    # get top 5 countries
    country_list = country_list[:5]

    # print header
    header = ""
    for i in range(70):
        header += "-"
    print(header)
    print(f"{'| Country':<35}" + f"{'| Trade Deficit (Billions USD)':<33} | ")  # each column is 35 char wide
    print(header)

    # print countries with their trade deficits
    for i in range(len(country_list)):
        print(f"| {country_list[i][1]:<33}" + f"{'| $'}" + f"{country_list[i][4]:>30.2f}" + " |")
    print(header)


def function_A():
    """
    A function for part A of the assignment.
    """
    country_list = load_file("country.txt")
    country_list = find_trade_deficits(country_list)
    country_list = sort_deficits(country_list)
    show_deficits(country_list)
    return country_list

"""
### --- SECTION B --- ###
1. Products per industry
    2. Exclusive products
    3. Countries with most exclusive products
    4. Industries with the fewest exclusives
    5. Most productive countries
    6. Most widespread products
"""

### --- Section B Question 1 --- ###
def products_per_industry(product_list):
    """
    input: product_list (list)
    process: Counts how many products belong to each industry
    return: industry_list (sorted list)
    """

    # a list of form [[industry, #]]
    # because dictionaries are a pain to sort
    industry_list = []
    industry_number = []

    # count how many products belong to each industry
    for i in range(len(product_list)):
        # if product already exists in industry list, add 1 to the count
        if product_list[i][1] in industry_list:
            industry_number[industry_list.index(product_list[i][1])] += 1
        else:
            # if new industry, add to industry list and start count
            industry_list.append(product_list[i][1])
            industry_number.append(1)

    # sort the list alphabetically
    industry_list.sort()

    return industry_list, industry_number


def show_product_per_industry(industry_list, industry_number):
    """
    input: industry_list (list), industry_number (list)
    process: Prints out a table showing the number of products per industry in alphabetical order of industries
    return: none
    """
    # print header
    header = ""

    for i in range(40):
        header += "-"
    print(header)
    print(f"{'| Industry':<18}" + f"{'| Number of Products':<18} | ")  # each column is 35 char wide
    print(header)

    # print industries with the number of products
    for i in range(len(industry_list)):
        print(f"| {industry_list[i]:<16}" + f"|" + f"{industry_number[i]:>19}" + " |")
    print(header)


### --- Section B Question 2 --- ###

def get_product_name(exclusive_products):
    """
    input: exclusive_products (list)
    return: returns the product name from PID
    """
    return exclusive_products[1]


def exclusive_product(product_list, product_country_list, country_list):
    """
    A product is exclusive if only one country produces it.
    input: product_list (list), product_country_list (list), country_list (list)
    process: finds which products are exclusive
    return: exclusive_products (sorted list, alphabetical by product name)
    [[PID, product name, product country name], etc.]
    """

    # find exclusive products with which countries produce it
    exclusive_products = []
    exclusive_countries = []
    for i in range(len(product_country_list)):
        # if the product is not on the list before
        if product_country_list[i][0] not in exclusive_products:
            exclusive = True
            # go down list
            for j in range(len(product_country_list)):
                # if the product ID matches and the country is different
                if product_country_list[j][0] == product_country_list[i][0] and product_country_list[j][1] != \
                        product_country_list[i][1]:
                    # no longer exclusive
                    exclusive = False
            if exclusive:
                exclusive_products.append(product_country_list[i][0])
                exclusive_countries.append(product_country_list[i][1])

    # pair products with the product name
    for i in range(len(exclusive_products)):
        for j in range(len(product_list)):
            if exclusive_products[i] == product_list[j][0]:
                exclusive_products[i] = [exclusive_products[i], product_list[j][2]]

    # pair products with the producing country name
    for i in range(len(exclusive_countries)):
        for j in range(len(country_list)):
            if exclusive_countries[i] == country_list[j][0]:
                exclusive_products[i].append(country_list[j][1])

    # check for countries without name matches
    for i in range(len(exclusive_products)):
        if len(exclusive_products[i]) == 2:
            exclusive_products[i].append(exclusive_countries[i])

    # sort alphabetically by product name
    exclusive_products.sort(key=get_product_name)

    return exclusive_products


def show_exclusive_products(exclusive_products):
    """
    input: exclusive_products (list) [[PID, product name, country], etc.]
    process: prints out the information in a table
    return: none
    """

    # print header
    header = ""

    for i in range(110):  # length of table
        header += "-"
    print(header)
    print(f"{'| PID':<15}" + f"{'| Product Name':<50} | " + f"{'Producing Country':<40} | ")
    print(header)

    # print table information
    for i in range(len(exclusive_products)):
        print(
            f"| {exclusive_products[i][0]:<13}" + f"| " + f"{exclusive_products[i][1]:<48}" + " | " + f"{exclusive_products[i][2]:<40}" + " |")
    print(header)

### --- Section B Question 3 --- ###

### Common Functions
def count(item_list, index):
    """
    input:
    - item_list (list)
        The list of items to iterate through
    - index (int)
        The index of the item to which the count is assigned to (such as industry or country).
        Of form list[i][index].

    process: creates a dictionary with key: item value: count
    - count (int)
        The number of counts belonging to an item

    returns: count_dict (dict)
    """

    # create the dictionary
    count_dict = {}

    # get the counts for the item
    for i in range(len(item_list)):
        if item_list[i][index] not in count_dict.keys():
            count_dict[item_list[i][index]] = 1
        else:
            count_dict[item_list[i][index]] += 1

    return count_dict

def sort_dict(dict):
    """
    input: dict (dict)
    process: sorts the dictionary in the descending order, by value
    return: sorted_list (list)
    """

    sorted_list = []
    for key, value in sorted(dict.items(), key=lambda item: item[1], reverse=True):
        sorted_list.append([key, value])

    return sorted_list

def sublist(list, order):
    """
    list: list (list), order
        - list: of form [[item, count], [item2, count], etc]
        - if order True: take sublist of ties between the highest entries
        - if order False: take sublist of ties between the lowest entries
    process: creates a sublist of the highest or lowest entries in the list
    return: sublist (list)
    """

    sublist = []
    if not order:
        list.reverse()
    for i in range(len(list)):
        if list[i][1] == list[0][1]:
            sublist.append(list[i])

    return sublist

def print_table(cols, length, titles, data):
    """
    input:
    - cols (int): the number of columns wanted
    - length (list): [length of column 1, length of column 2, etc.]
    - titles (list): [title for column 1, title for column 2, etc.]
    - data (list): a list of data to populate the table with
    process: prints a table with the specified data
    return: none
    """

    # construct the header
    header = ""
    if cols == 2:
        for i in range(sum(length) + 7):
            header += "-"
    elif cols == 3:
        for i in range(sum(length) + 10):
            header += "-"

    # print the first row (title row)
    print(header)
    if cols == 2:
        print('| ' + f"{titles[0]:<{length[0]}}" + " | " + f"{titles[1]:<{length[1]}}" + " |")
    elif cols == 3:
        print('| ' + f"{titles[0]:<{length[0]}}" + " | " + f"{titles[1]:<{length[1]}}" + " | " + f"{titles[2]:<{length[2]}}")
    print(header)

    # print table information
    if cols == 2:
        for i in range(len(data)):
            print("| " + f"{data[i][0]:<{length[0]}}" + f" | " + f"{data[i][1]:<{length[1]}}" + " |")
    elif cols == 3:
        for i in range(len(data)):
            print("| " + f"{data[i][0]:<{length[0]}}" + f" | " + f"{data[i][1]:<{length[1]}}" + " | " + f"{data[i][2]:<{length[2]}}" + " |")
    print(header)

### Question 3 Functions

def find_most_exclusive_products(exclusive_products):
    """
    input: exclusive_products (list) [[PID, product name, country], etc.]
    Find the country with the most exclusive products. if there is a tie, sort alphabetically. Print out in a table.
    return: none
    """

    # get the number of exclusive products per country in a dictionary
    exclusive_products_dict = count(exclusive_products, 2)
    # sort the dictionary in descending order
    sorted_exclusive_products = sort_dict(exclusive_products_dict)
    # get the sublist of countries with the highest number of exclusive products
    highest_products = sublist(sorted_exclusive_products, True)
    # sort alphabetically
    highest_products.sort()
    # print out in a table
    print_table(2, [15, 28], ['Country', 'No. of Exclusive Products'], highest_products)

### --- Section B Question 4 --- ###

def find_fewest_exclusives(product_list, exclusive_products):
    """
    input: product_list (list), exclusive_products  [[PID, product name, country], etc.]
    process: find the industry with the least number of exclusive products
    return: lowest_industries (list)
    """

    # match exclusive products with industry
    for i in range(len(exclusive_products)):
        for j in range(len(product_list)):
            if exclusive_products[i][0] == product_list[j][0]:
                exclusive_products[i].append(product_list[j][1])

    # get the number of exclusive products per industry in a dictionary
    exclusive_by_industry = count(exclusive_products, 3)
    # sort the dictionary in descending order
    sorted_exclusive_by_industry = sort_dict(exclusive_by_industry)
    # get the sublist of countries with the lowest number of exclusive products
    lowest_industries = sublist(sorted_exclusive_by_industry, False)
    # sort alphabetically
    lowest_industries.sort()
    # print out in a table
    print_table(2, [15, 28], ['Industry', 'No. of Exclusive Products'], lowest_industries)

### --- Section B Question 5 --- ###

def find_most_productive_country(product_country_list, country_list):
    """
    input: product_country_list (list), country_list (list)
    process: finds the most productive country and prints in a table
    return: none
    """

    # get the number of products per country in a dictionary
    most_productive = count(product_country_list, 1)
    # sort the dictionary in descending order
    sorted_most_productive = sort_dict(most_productive)
    # get the sublist of countries with the most amount of products
    most_productive_countries = sublist(sorted_most_productive, True)
    # sort alphabetically
    most_productive_countries.sort()
    # match with country name
    for i in range(len(most_productive_countries)):
        for j in range(len(country_list)):
            if most_productive_countries[i][0] == country_list[j][0]:
                most_productive_countries[i][0] = country_list[j][1]
    # print out in a table
    print_table(2, [15, 20], ['Country', 'Number of Products'], most_productive_countries)

### --- Section B Question 6 --- ###

def find_most_widespread_products(product_country_list, product_list):
    """
    input: product_country_list (list), product_list (list)
    """

    # get the number of countries per product in a dictionary
    most_widespread = count(product_country_list, 0)
    # sort the dictionary in descending order
    sorted_most_widespread = sort_dict(most_widespread)
    # get the sublist of products with the most widespread countries

    print(sorted_most_widespread)

    # get the top 3 values
    top_values = []
    tally = 0
    for i in range(len(sorted_most_widespread)):
        if tally <= 3:
            # top value
            if tally == 0:
                top_values.append(sorted_most_widespread[0][1])
                tally += 1
            # 2nd top value
            if tally == 1 and sorted_most_widespread[i][1] < top_values[0]:
                top_values.append(sorted_most_widespread[i][1])
                tally += 1
            # 3rd top value
            if tally == 2 and sorted_most_widespread[i][1] < top_values[1]:
                top_values.append(sorted_most_widespread[i][1])
                tally += 1

    print(top_values)

    # get a sublist with those values
    top_widespread_products = []
    for i in range(len(sorted_most_widespread)):
        if sorted_most_widespread[i][1] in top_values:
            top_widespread_products.append(sorted_most_widespread[i])

    # match with product name
    for i in range(len(top_widespread_products)):
        for j in range(len(product_list)):
            if top_widespread_products[i][0] == product_list[j][0]:
                top_widespread_products[i][0] = product_list[j][2]

    # sort by number and then product name alphabetically
    top_widespread_products.sort(key=lambda item: (-item[1], item[0]), reverse=False)

    # print out in a table
    print_table(2, [50, 15], ['Product Name', 'Number of Countries'], top_widespread_products)

### --- Section B Master Function --- ###

def function_B(country_list):
    """
    A function for part B of the assignment.
    """

    ### --- Products per Industry --- ###
    product_list = load_file("product.txt")
    industry_list, industry_number = products_per_industry(product_list)
    show_product_per_industry(industry_list, industry_number)

    ### --- Exclusive Products --- ###
    product_country_list = load_file("product_country.txt")
    exclusive_products = exclusive_product(product_list, product_country_list, country_list)
    show_exclusive_products(exclusive_products)

    ### --- Countries with most exclusive products --- ###
    find_most_exclusive_products(exclusive_products)

    ### --- Industries with Fewest Exclusives --- ###
    find_fewest_exclusives(product_list, exclusive_products)

    ### --- Most Productive Countries --- ###
    find_most_productive_country(product_country_list, country_list)

    ### --- Most Widespread Products --- ###
    find_most_widespread_products(product_country_list, product_list)

if __name__ == "__main__":
    country_list = function_A()
    function_B(country_list)

"""
### --- SECTION C --- ###
1. Outrageous Tarrifs: identify countries that face 50% on one or more of their industries
2. Tariff-Free Countries: identify countries with no tariffs at all imposed on them
3. Selective Tariff Countries: identify countries that have tariffs on some industries but not on others
"""
