# bus_routes.py

"""
Title: Lab 1
Author: Alice Cai
Date: 2026-01-17
"""

"""
Project description: 
An ETS transit planner. Given a start and end destination, the program can search for a direct bus route or find a single-transfer route.

Requirements:
Input validation is NOT required unless stated. 
Do not use break/continue in loops.
Use of external libraries is prohibited. 
"""

"""
Files Given:

routes: describes each ETS route and its stop code sequences
    <Transit line>,<stop 1>,<stop 2>,<stop 3>...<stop N>
codes: maps each stop code to the stop name
    <code>,<Stop Name>
"""

def load_file(filename):
    """
    input: filename (str)
    process: opens a file and puts it into a dictionary
    return: routes (dict)
    """

    # open the file and get as list
    with open(filename, 'r') as file:
        data = file.readlines()

    # strip the \n from the end of each line and split lines into lists
    for i in range(len(data)):
        data[i] = data[i].strip()
        data[i] = data[i].split(",")

    # place into dictionary
    data_dict = {}
    for i in range(len(data)):

        # routes-specific data processing
        # key: the route number (the first value in the list)
        # value: a list of the route stops (the remaining values in the list)
        
        if filename == "routes.txt":
            data_dict[data[i][0]] = data[i][1:]

        # codes-specific data processing
        # key: the stop code
        # value: the name of the stop/station

        elif filename == "codes.txt":
            data_dict[data[i][0]] = data[i][1]

    # close the file
    file.close()

    return data_dict

def lookup(station_name, codes):
    """
    input: station_name (str), codes (dict)
    process: given a stop/station name, looks up the corresponding stop code
    assumes that the station names are unique and exist in the codes dictionary
    return: station_code (str)
    """

    station_code = ""
    for key, value in codes.items():
        if value == station_name:
            station_code = key

            return station_code

def get_stop_names(route_number, routes, codes):
    """
    input: route_number (str), routes (dict), codes (dict)
    process: given a route number, makes a string with all the stops on that route
    return: stop_names_string (str)
    """

    all_route_codes = routes[route_number]  # a list of all the stop codes associated with the route number
    stop_names = []  # a list of all the stop names associated with each stop code

    # get all stop names
    for i in range(len(all_route_codes)):
            stop_names.append(codes[all_route_codes[i]])

    # join stops together
    stop_names_string = " -> ".join(stop_names)

    return stop_names_string


def find_direct_route(routes, codes, starting_point, destination):
    """
    A direct route exists if any route (bidirectional) contains both the start code and destination code.
    input: routes (dict), codes(dict), starting_point (str), destination (str) that are the stop names
    process: searches for a direct bus route from starting point to destination and prints it out
    return: True if a direct route exists, False if not
    """

    # convert starting point and destination names into stop codes
    start_code = lookup(starting_point, codes)
    end_code = lookup(destination, codes)

    # check if there is a direct route possible
    # iterating through the dictionary, if both the start and end stop are on the route, a direct route exists
    direct_route = None
    for key, value in routes.items():
        if start_code in value and end_code in value:
            direct_route = key # the route number of the direct route

    #---if a direct route exists---#
    if direct_route is not None: 

        # get the names of all stops
        direct_route_stops = get_stop_names(direct_route, routes, codes)

        # print direct route
        print(f"Direct route found: {direct_route} -> {direct_route_stops}")

        return True

    #---no direct route exists---#
    else:
        return False

def find_transfer(routes, codes, starting_point, destination):
    """
    Find a single-transfer route where starting point --> route 1 --> get off at stop A --> take route 2 to destination
    input: routes (dict), codes (dict), starting_point (str), destination (str) that are stop names
    return: True if transfer possible, False if not
    """

    # convert starting point and destination into codes
    start_code = lookup(starting_point, codes)
    end_code = lookup(destination, codes)

    # find routes with the start or end code
    start_routes = []
    end_routes = []

    for key, value in routes.items(): 
        # routes containing the start code
        if start_code in value:
            start_routes.append(key)
        # routes containing the end code
        if end_code in value:
            end_routes.append(key)

    #--- for every pair of routes, check if there are stops in common---#
    intersection = [] # a list of stops that 2 routes have in common

    # for every distinct pair of routes
    for i in range(len(start_routes)):
        for j in range(len(end_routes)):

            # get the list of stop codes on that route
            start_routes_codes = routes[start_routes[i]]
            end_routes_codes = routes[end_routes[j]]

            # find the intersection between the two routes
            # there may be multiple options in intersection; the program takes the first
            intersection = list(set(start_routes_codes) & set(end_routes_codes)) 

            # convert intersection code to stop name
            for k in range(len(intersection)):
                intersection[i] = codes[intersection[k]]

            # --- if there is a transfer option found --- #
            if len(intersection) != 0:
            
                # print out transfer
                print("")
                print("Transfer option found:")
                print("")
                print(f"Take route {start_routes[i]} and get off at {intersection[0]}.")  # take the first transfer option
                print(f"Then take route {end_routes[j]} to your destination.")

                #--- print out exact transfer route---#

                # get the path string for each route
                start_route_names = get_stop_names(start_routes[i], routes, codes)
                end_route_names = get_stop_names(end_routes[j], routes, codes)

                print("")
                print(f"Route {start_routes[i]}: {start_route_names}")  # print out the route number followed by path
                print(f"Route {end_routes[j]}: {end_route_names}")

                return True

    # if no transfer options found
    return False


def main():
    
    ## --- SETUP --- ##
    # get the starting point and destination from user
    starting_point = input("Enter Starting Point: ").title()  # stop names are in title case
    destination = input("Enter Destination: ").title()

    # load routes and codes files into dictionaries
    routes = load_file("routes.txt")
    codes = load_file("codes.txt")    

    ## --- PROCESS --- ##
    # find direct route
    direct_route_exists = find_direct_route(routes, codes, starting_point, destination)

    # find route with transfer
    if not direct_route_exists:
        transfer_exists = find_transfer(routes, codes, starting_point, destination)

        if not transfer_exists:
        # neither a direct route or valid single-transfer route
            print("No routes serving that start point and end point")


if __name__ == "__main__":
    main()