"""
    # Place country data into dictionary
    # Country code is key, value is a list [country name, imports, exports]
    # also convert import and export to floats

    country_dict = {}

    for i in range(len(data)):
        if i != 0: # exclude title row
            country_dict[data[i][0]] = [data[i][1], float(data[i][2]), float(data[i][3])]
    """

"""
for key, value in country_dict.items():
    country_dict[key] = value + [value[1]-value[2]]
"""

"""
# convert back to list
keys = list(country_dict.keys())
values = list(country_dict.values())
for i in range(len(values)):
    values[i].insert(0, keys[i])
"""