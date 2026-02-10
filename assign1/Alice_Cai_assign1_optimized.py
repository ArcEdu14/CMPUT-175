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

        # exclude title row
        data = data[1:]

        # convert to int
        for i in range(len(data)):
            data[i][2] = int(data[i][2])
        return data

    elif filename == "tariff.txt":
        # spaces present between 1st and second col, not between 2nd and 3rd
        for i in range(len(data)):
            data[i] = data[i].split(",")

        # exclude title row
        data = data[1:]

        # convert percentages to int
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] = data[i][j].strip()
            data[i][2] = int(data[i][2])

        return data

    elif filename == "shopping_list.txt":
        for i in range(len(data)):
            data[i] = data[i].strip()
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
    process: returns the trade deficit of a country (used for sorting)
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


def function_A(country_list):
    """
    A function for part A of the assignment.
    """
    country_list = find_trade_deficits(country_list)
    country_list = sort_deficits(country_list)
    show_deficits(country_list)

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
    for country in exclusive_products:
        if len(country) == 2:
            exclusive_products.remove(country)

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
        print(f"| {exclusive_products[i][0]:<13}" + f"| " + f"{exclusive_products[i][1]:<48}" + " | " + f"{exclusive_products[i][2]:<40}" + " |")
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
    if cols == 1:
        for i in range(sum(length) + 4):
            header += "-"
    if cols == 2:
        for i in range(sum(length) + 7):
            header += "-"
    elif cols == 3:
        for i in range(sum(length) + 10):
            header += "-"
    elif cols == 7:
        for i in range(sum(length) + 22):
            header += "-"

    # print the first row (title row)
    print(header)
    if cols == 1:
        print('| ' + f"{titles[0]:<{length[0]}}" + " |")
    elif cols == 2:
        print('| ' + f"{titles[0]:<{length[0]}}" + " | " + f"{titles[1]:<{length[1]}}" + " |")
    elif cols == 3:
        print('| ' + f"{titles[0]:<{length[0]}}" + " | " + f"{titles[1]:<{length[1]}}" + " | " + f"{titles[2]:<{length[2]}}")
    elif cols == 7:
        print('| ' + f"{titles[0]:<{length[0]}}" + " | " + f"{titles[1]:<{length[1]}}" + " | " + f"{titles[2]:<{length[2]}}" + " | " + f"{titles[3]:<{length[3]}}" + " | " + f"{titles[4]:<{length[4]}}" + " | " + f"{titles[5]:<{length[5]}}" + " | " + f"{titles[6]:<{length[6]}}" + " |")
    print(header)

    # print table information
    if cols == 1:
        for i in range(len(data)):
            print('| ' + f"{data[i]:<{length[0]}}" + " |")
    elif cols == 2:
        for i in range(len(data)):
            print("| " + f"{data[i][0]:<{length[0]}}" + f" | " + f"{data[i][1]:<{length[1]}}" + " |")
    elif cols == 3:
        for i in range(len(data)):
            print("| " + f"{data[i][0]:<{length[0]}}" + f" | " + f"{data[i][1]:<{length[1]}}" + " | " + f"{data[i][2]:<{length[2]}}" + " |")
    elif cols == 7:
        for i in range(len(data)):
            print("| " + f"{data[i][0]:<{length[0]}}" + f" | " + f"{data[i][1]:<{length[1]}}" + " | " + f"{data[i][2]:<{length[2]}}" + " | " + f"{'$'}" + f"{data[i][3]:>{length[3]-1},.2f}" + " | " + f"{data[i][4]:>{length[4]-1},.1f}" + "%" " | " + f"{'$'}" + f"{data[i][5]:>{length[5]-1},.2f}" + " | " + f"{'$'}" + f"{data[i][6]:>{length[6]-1},.2f}" + " |")
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
    ### get the sublist of products with the most widespread countries
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
    print_table(2, [50, 20], ['Product Name', 'Number of Countries'], top_widespread_products)

### --- Section B Master Function --- ###

def function_B(product_list, product_country_list, country_list):
    """
    A function for part B of the assignment.
    """

    ### --- Products per Industry --- ###
    industry_list, industry_number = products_per_industry(product_list)
    show_product_per_industry(industry_list, industry_number)

    ### --- Exclusive Products --- ###
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

    return product_list

"""
### --- SECTION C --- ###
1. Outrageous Tariffs: identify countries that face 50% on one or more of their industries
2. Tariff-Free Countries: identify countries with no tariffs at all imposed on them
3. Selective Tariff Countries: identify countries that have tariffs on some industries but not on others
"""

### Common Functions
def match_country(code_list, country_list):
    """
    Given the country code, finds the country name
    :param code_list: list
    :param country_list: list
    :return: updated code_list
    """
    for i in range(len(code_list)):
        for j in range(len(country_list)):
            if code_list[i] == country_list[j][0]:
                code_list[i] = country_list[j][1]
    return code_list

### --- Section C Question 1 --- ###
def identify_outrageous_tariffs(tariff_list, country_list):
    """
    input: tariff_list (list), country_list (list)
    process: finds the countries with tariffs over 50% and prints out in a nice table
    return: tariffs (list of list containing dictionary)
    """

    # a list of lists containing dictionaries
    # [[country, {industry: tariff, industry2: tariff2}], [country2, {industry: tariff}], etc.]
    tariffs = []

    # populate the list with countries
    for i in range(len(tariff_list)):
        if [tariff_list[i][0], {}] not in tariffs:
            tariffs.append([tariff_list[i][0], {}])

    # populate the country sublists with dictionaries
    for i in range(len(tariffs)):
        for j in range(len(tariff_list)):
            if tariff_list[j][0] == tariffs[i][0]:
                tariffs[i][1][tariff_list[j][1]] = tariff_list[j][2]

    # identify outrageous countries
    outrageous_countries = set()
    for i in range(len(tariffs)):
        for value in tariffs[i][1].values():
            if value > 50:
                outrageous_countries.add(tariffs[i][0])

    # convert set back into list and sort
    outrageous_countries = list(outrageous_countries)
    outrageous_countries.sort()

    # match country code with country
    outrageous_countries = match_country(outrageous_countries, country_list)

    # print countries with outrageous tariffs
    print_table(1, [40], ['Country'], outrageous_countries)

    return tariffs

### --- Section C Question 2 --- ###
def find_tariffed_countries(tariff_list):
    tariffed_countries = set()
    for i in range(len(tariff_list)):
        if tariff_list[i][2] != 0:
            tariffed_countries.add(tariff_list[i][0])
    return tariffed_countries

def identify_tariff_free(tariff_list, country_list):
    """
    input: tariff_list (list), country_list (list)
    process: finds a list of tariff-free countries
    return: none
    """
    tariff_free = set()
    for i in range(len(country_list)):
        if country_list[i][0] not in find_tariffed_countries(tariff_list):
            tariff_free.add(country_list[i][0])

    # convert back into sorted list
    tariff_free = list(tariff_free)
    tariff_free.sort()

    # match to country name
    tariff_free = match_country(tariff_free, country_list)

    # print table of tariff-free
    print_table(1, [40], ['Country'], tariff_free)

### --- Section C Question 3 --- ###

def identify_select_industries(tariff_masterlist, country_list):
    """
    input: tariff_masterlist (list of list containing dictionary)
    process: find and printindustries by country that are tariff-free
    return: none
    """

    select_industries = []

    # find industries without any tariffs
    for i in range(len(tariff_masterlist)):
        for industry in ['Agriculture', 'Manufacturing', 'Tech', 'Pharmacy', 'Food']:
            if industry not in tariff_masterlist[i][1].keys():
                select_industries.append([tariff_masterlist[i][0], industry])

    # match country code to country name
    for i in range(len(select_industries)):
        select_industries[i] = match_country(select_industries[i], country_list)

    # sort list
    select_industries.sort(key=lambda item: (item[0], item[1]))

    # print out table
    print_table(2, [40, 40], ['Country', 'Industry'], select_industries)

def function_C(tariff_list, country_list):
    """
    Master function for section C
    """
    tariff_masterlist = identify_outrageous_tariffs(tariff_list, country_list)
    identify_tariff_free(tariff_list, country_list)
    identify_select_industries(tariff_masterlist, country_list)
    return tariff_masterlist

"""
### --- SECTION D --- ###
Cheapest import strategy based on tariffs

Columns:
- product name 
- # of countries that produce the product
- country with the best price for the product including tariffs
- actual cost of product without tariffs
- tariff %
- tariff value
- total cost including tariffs
"""

def match_product(code_list, product_list):
    """
    input: code_list (list of codes to match to product name), product_list (list)
    process: replaces product codes with product names for new list
    return: new_list (2d list of names)
    """
    new_list = []
    for i in range(len(code_list)):
        for j in range(len(product_list)):
            if code_list[i] == product_list[j][0]:
                new_list.append([product_list[j][2]])

    return new_list

def get_industry(code, product_list):
    """
    Given a product code, finds the industry the product belongs to
    :param code: PID (str)
    :param product_list: list
    :return: the industry the product belongs to (str)
    """
    for i in range(len(product_list)):
        if code == product_list[i][0]:
            return product_list[i][1]

def find_countries_selling_product(table_list, shopping_list, product_country_list):
    """
    input: table_list (list of product names), shopping_list (list of PID), product_country_list (list of PIDs and countries)
    process: counts the number of countries that produce a product
    return: table_list (updated list)
    """

    # find the countries that sell the product
    countries_that_sell = []
    for i in range(len(shopping_list)):
        countries_that_sell.append([shopping_list[i], get_industry(shopping_list[i], product_list), {}])

    # populate with all the countries that sell the products
    for i in range(len(countries_that_sell)):
        for j in range(len(product_country_list)):
            if countries_that_sell[i][0] == product_country_list[j][0]:
                countries_that_sell[i][2][product_country_list[j][1]] = product_country_list[j][2]

    # I did this part before I found the countries that sell the product which is why its weird
    # get the number of countries selling product in a dictionary
    countries_selling_product_dict = count(product_country_list, 0)

    # search up shopping list PIDs in dictionary
    for i in range(len(shopping_list)):
        # append to the master list
        table_list[i].append(countries_selling_product_dict[shopping_list[i]])

    return table_list, countries_that_sell

def get_tariff_rate(country, industry, tariff_masterlist):
    """
    Finds the tariff rate of an industry given the country and masterlist
    :param country: the country you wish to buy from (str)
    :param industry: the industry you wish to buy from (str)
    :param tariff_masterlist: list
    :return: the rate as a fraction
    """
    for i in range(len(tariff_masterlist)):
        if country == tariff_masterlist[i][0]:
            rate = tariff_masterlist[i][1][industry]
            return rate/100

def apply_tariffs(industry, dict, tariff_masterlist):
    """
    Creates a new dictionary with each country's tariffed product price
    :param industry: the industry of the product you want to buy from
    :param dict: a dictionary to update with the tariff prices
    :param tariff_masterlist: list
    :return: a new dictionary with tariff rates applied to product prices
    """
    new_dict = {}
    for key, value in dict.items():
        new_dict[key] = value * (1+get_tariff_rate(key, industry, tariff_masterlist))

    return new_dict

def calculate_new_price(countries_that_sell, tariff_masterlist):
    """
    Calculates the new price for each country per product after applying tariffs
    :param countries_that_sell: list
    :param tariff_masterlist: list
    :return: updated countries_that_sell list
    """
    for i in range(len(countries_that_sell)):
        # appending a new dictionary with updated prices to the end of each product entry
        countries_that_sell[i].append(apply_tariffs(countries_that_sell[i][1], countries_that_sell[i][2], tariff_masterlist))

    return countries_that_sell

def choose_best_country(countries_that_sell):
    """
    From the tariffed prices, chooses the country and price that is the lowest and adds it to the list
    :param countries_that_sell: list
    :return: updated countries_that_sell
    """
    for i in range(len(countries_that_sell)):
        all_prices = []
        for country, price in countries_that_sell[i][3].items():
            all_prices.append([country, price])

        # I think I could use min() here instead
        best_price = all_prices[0][1]
        best_country = all_prices[0][0]
        for j in range(len(all_prices)):
            if all_prices[j][1] < best_price:
                best_price = all_prices[j][1]
                best_country = all_prices[j][0]
        countries_that_sell[i].append([best_country, best_price])

    return countries_that_sell

def apply_best_country(countries_that_sell, table_list, tariff_masterlist, country_list):
    """
    Updates table_list with all the information needed for the table
    :param countries_that_sell: list
    :param table_list: list (to print)
    :param tariff_masterlist: list
    :return: table_list (list)
    """

    for i in range(len(table_list)):
        # best country
        best_country = countries_that_sell[i][4][0]
        table_list[i].append(match_country([best_country], country_list)[0])
        # actual cost (original price)
        table_list[i].append(countries_that_sell[i][2][best_country])
        # tariff %
        rate = get_tariff_rate(countries_that_sell[i][4][0], countries_that_sell[i][1], tariff_masterlist)
        table_list[i].append(rate*100)
        # tariff Val
        table_list[i].append(table_list[i][3]*rate)
        # Total cost
        table_list[i].append(countries_that_sell[i][4][1])

    return table_list

def get_summary_data(table_list):
    """
    Calculates the summary data of cost before tariff, total tariff paid, and grand total
    :param table_list: list
    :return: list [cost before tariff, total tariff paid, grand total]
    """
    summary_data = [0, 0, 0]
    for i in range(len(table_list)):
        summary_data[0] += table_list[i][3]
        summary_data[1] += table_list[i][5]
        summary_data[2] += table_list[i][6]

    return summary_data


def print_shopping_list(table_list, summary_data):
    """
    Prints the shopping list table and summaries
    :param table_list: list
    :return:
    """
    print_table(7, [25, 10, 20, 15, 15, 15, 15], ['Product Name', 'Countries', 'Best Country', 'Actual Cost', 'Tariff %', 'Tariff Val', 'Total Cost'], table_list)

    print(f"Cost before Tariff: $ {summary_data[0]:,.2f}")
    print(f"Total Tariff Paid: $ {summary_data[1]:,.2f}")
    print(f"Grand Total: $ {summary_data[2]:,.2f}")

def function_D(product_list, shopping_list, product_country_list, tariff_masterlist):
    """
    Master function for section D
    """
    # get the PIDs from shopping_list and replace with the actual product names
    table_list = match_product(shopping_list, product_list)

    # find the number of countries that sell the product
    # also creates a list countries_that_sell with each product in [product_name, industry, {country: price}]
    table_list, countries_that_sell = find_countries_selling_product(table_list, shopping_list, product_country_list)

    # calculate tariffs and choose the best country
    # after calculating tariffed prices, append to each entry countries_that_sell [product_name, industry, {country: price}, {country: new price}]
    countries_that_sell = calculate_new_price(countries_that_sell, tariff_masterlist)
    # append the best country to buy from according to tariffed prices to each entry [best_country, best_price]
    countries_that_sell = choose_best_country(countries_that_sell)

    # add the best country to table list
    table_list = apply_best_country(countries_that_sell, table_list, tariff_masterlist, country_list)

    # get summary data
    summary_data = get_summary_data(table_list)

    # print it out
    print_shopping_list(table_list, summary_data)


if __name__ == "__main__":
    # Load all files
    country_list = load_file("country.txt")
    product_list = load_file("product.txt")
    product_country_list = load_file("product_country.txt")
    shopping_list = load_file("shopping_list.txt")
    tariff_list = load_file("tariff.txt")

    # Run all functions
    print("### --- SECTION A --- ###")
    function_A(country_list)
    print("### --- SECTION B --- ###")
    function_B(product_list, product_country_list, country_list)
    print("### --- SECTION C --- ###")
    tariff_masterlist = function_C(tariff_list, country_list)
    print("### --- SECTION D --- ###")
    function_D(product_list, shopping_list, product_country_list, tariff_masterlist)