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
            if i != 0: # exclude title row
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
        country_list[i].append(country_list[i][2]-country_list[i][3])

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

    """
    
    exclusive_products = []
    exclusive_countries = []
    
    for i in range(len(product_country_list)):
        if product_country_list[i][0] not in exclusive_products:
            exclusive_products.append(product_country_list[i][0])
            exclusive_countries.append(product_country_list[i][1])
        else:
            if product_country_list[i][1] == 
            
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
                if product_country_list[j][0] == product_country_list[i][0] and product_country_list[j][1] != product_country_list[i][1]:
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
        print(f"| {exclusive_products[i][0]:<13}" + f"| " + f"{exclusive_products[i][1]:<48}" + " | " + f"{exclusive_products[i][2]:<40}" + " |")
    print(header)

def most_exclusive_products(exclusive_products):
    """
    input: exclusive_products (list) [[PID, product name, country], etc.]
    Find the country with the most exclusive products. if there is a tie, sort alphabetically.
    return: top result for most exclusive product (list)
    """

    # Try to use a dictionary this time
    exclusive_products_dict = {}

    # get all countries with exclusive products
    for i in range(len(exclusive_products)):
        if exclusive_products[i][2] not in exclusive_products_dict.keys():
            exclusive_products_dict[exclusive_products[i][2]] = 1
        else:
            exclusive_products_dict[exclusive_products[i][2]] += 1

    # sort dictionary by most and alphabetical
    sorted_exclusive_products = []
    for key, value in sorted(exclusive_products_dict.items(), key = lambda item: item[1], reverse = True):
        sorted_exclusive_products.append([key, value])

    # get sublist of highest
    highest_products = []
    for i in range(len(sorted_exclusive_products)):
        if sorted_exclusive_products[i][1] == sorted_exclusive_products[0][1]:
            highest_products.append(sorted_exclusive_products[i])

    # sort alphabetically
    highest_products.sort()

    return highest_products[0]

def show_most_exclusive_products(highest):
    """
    input: [country, number of exclusive products]
    process: prints out a table with the information
    """
    # print header
    header = ""

    for i in range(50):  # length of table
        header += "-"
    print(header)
    print(f"{'| Country':<18}" + f"{'| No. of Exclusive Products':<30} | ")
    print(header)

    # print table information
    print(f"| {highest[0]:<16}" + f"| " + f"{highest[1]:<28}" + " | " )
    print(header)

def fewest_exclusives(product_list, exclusive_products):
    """
    input: product_list (list), exclusive_products  [[PID, product name, country], etc.]
    process: find the industry with the least number of exclusive products
    return: lowest_industries (list)
    """

    # a dictionary with key: industry value: number of exclusive products
    exclusive_by_industry = {}

    # match exclusive products with industry
    for i in range(len(exclusive_products)):
        for j in range(len(product_list)):
            if exclusive_products[i][0] == product_list[j][0]:
                exclusive_products[i].append(product_list[j][1])

    # count number of exclusive products per industry
    for i in range(len(exclusive_products)):
        if exclusive_products[i][3] not in exclusive_by_industry.keys():
            exclusive_by_industry[exclusive_products[i][3]] = 1
        else:
            exclusive_by_industry[exclusive_products[i][3]] += 1

    # sort dictionary by least number of exclusive products
    sorted_exclusive_by_industry = []
    for key, value in sorted(exclusive_by_industry.items(), key=lambda item: item[1]):
        sorted_exclusive_by_industry.append([key, value])

    # get sublist of lowest
    lowest_industries = []
    for i in range(len(sorted_exclusive_by_industry)):
        if sorted_exclusive_by_industry[i][1] == sorted_exclusive_by_industry[0][1]:
            lowest_industries.append(sorted_exclusive_by_industry[i])

    # sort alphabetically
    lowest_industries.sort()

    return lowest_industries[0]

def show_fewest_exclusives(lowest):
    """
    input: lowest [industry, number of exclusive products]
    process: prints out a table with the information
    return: none
    """
    # print header
    header = ""

    for i in range(50):  # length of table
        header += "-"
    print(header)
    print(f"{'| Industry':<18}" + f"{'| No. of Exclusive Products':<30} | ")
    print(header)

    # print table information
    print(f"| {lowest[0]:<16}" + f"| " + f"{lowest[1]:<28}" + " | ")
    print(header)

def most_productive_country(product_country_list, country_list):
    """
    input: product_country_list (list), country_list (list)
    process: finds the most productive country
    return: highest_countries (list)
    """

    # dictionary with key: country code value: number of products
    most_productive = {}

    # count number of products per country
    for i in range(len(product_country_list)):
        if product_country_list[i][1] not in most_productive.keys():
            most_productive[product_country_list[i][1]] = 1
        else:
            most_productive[product_country_list[i][1]] += 1

    # sort dictionary by least number of exclusive products
    sorted_most_productive = []
    for key, value in sorted(most_productive.items(), key=lambda item: item[1], reverse=True):
        sorted_most_productive.append([key, value])

    # get sublist of highest
    highest_countries = []
    for i in range(len(sorted_most_productive)):
        if sorted_most_productive[i][1] == sorted_most_productive[0][1]:
            highest_countries.append(sorted_most_productive[i])

    # sort alphabetically
    highest_countries.sort()

    # match with country name
    for i in range(len(highest_countries)):
        for j in range(len(country_list)):
            if highest_countries[i][0] == country_list[j][0]:
                highest_countries[i].append(country_list[j][1])

    return highest_countries[0]

def show_most_productive_country(highest):
    """
    input: highest [country code, number of products, country name]
    process: prints out a table with the information
    return: none
    """
    # print header
    header = ""

    for i in range(50):  # length of table
        header += "-"
    print(header)
    print(f"{'| Country':<18}" + f"{'| No. of Products':<30} | ")
    print(header)

    # print table information
    print(f"| {highest[2]:<16}" + f"| " + f"{highest[1]:<28}" + " | " )
    print(header)

def function_B(country_list):
    """
    A function for part B of the assignment.
    1. Products per industry
    2. Exclusive products
    3. Countries with most exclusive products
    4. Industries with the fewest exclusives
    5. Most productive countries
    6. Most widespread products
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
    highest = most_exclusive_products(exclusive_products)
    show_most_exclusive_products(highest)

    ### --- Industries with Fewest Exclusives --- ###
    lowest = fewest_exclusives(product_list, exclusive_products)
    show_fewest_exclusives(lowest)

    ### --- Most Productive Countries --- ###
    most_productive = most_productive_country(product_country_list, country_list)
    show_most_productive_country(most_productive)

    ### --- Most Widespread Products --- ###

if __name__ == "__main__":
    country_list = function_A()
    function_B(country_list)

