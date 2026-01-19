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

def function_A(country_filename):
    """
    """

    ### --- Load Country File --- ###

    with open(country_filename, "r") as file:
        data = file.readlines()  # list

    # strip \n and split into list
    for i in range(len(data)):
        data[i] = data[i].strip()  
        data[i] = ",".split(data[i])  

    # Place country data into dictionary
    # Country code is key, value is a list [country name, imports, exports]

    country_dict = {}

    for i in range(len(data)):
        country_dict[data[i][0]] = data[i][1:]

    print(country_dict)


if __name__ == "__main__":
    function_A("country.txt")

