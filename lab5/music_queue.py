# =================================================================
# CMPUT 175 - Introduction to the Foundations of Computation II
# Lab 5 - Music Queue
#
# ~ Created by CMPUT 175 Team ~
# Completed by Alice Cai
# Date: 2026-03-02
# =================================================================

"""
Program Description:

A music player that searches Youtube, adds songs, plays next, displays queue.
To run from terminal: python "C:\Users\Alice C\PycharmProjects\CMPUT-175\lab5\music_queue.py"
"""

# Install ytmusicapi using pip or pip3
from ytmusicapi import YTMusic
from structures import MusicQueue, Song, time_to_seconds
import os

NO_OF_RESULTS = 5

# DO NOT MODIFY
def clear():
    """
    Input: None
    Returns: None
    Working:
    This function clears terminal screen
    """
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')

def extract_artists(song_info):
    """
    Input: Data of the song as originally retrieved (dictionary format)
    Returns: All artists involved in the song as a string or "NA" if no artist info is available.
    Working:
    This function makes sure that all artists involved in a song show up in the final 
    representation.
    """
    try:
        artists = ""
        # if o artist information is available (empty list)
        if len(song_info) == 0:
            return "NA"
        # for each artist in the list
        for name in song_info:
            artists += name['name'] + ", "  # concatenate with comma seperator
        return artists[0:len(artists)-2]  # cut off last comma and space
    # Error occurred
    except:
        raise Exception("Artist error")

def song_search(query):
    """
    Input: Search query
    Returns: Top 5 results from the retrieved data
    Working:
    This function invokes the search method on YTMusic object with required arguments
    and returns the top "NO_OF_RESULTS" results.
    """
    # create YT music object
    yt_music = YTMusic()
    return yt_music.search(query, filter = "songs", scope =None)[0:5]  # top 5 results

def filter_info(results):
    """
    Input: Search results in a JSON like format
    Returns: List of Song Objects
    Working:
    This function is supposed to extract the required information from the JSON,
    create Song objects and append them to a list. If an error occurs, raise an
    exception.
    """
    # results in list of dict format [{'category': 'Songs', 'resultType': 'song', 'title': 'title', 'album': {'name': 'name', 'id': 'id'}, 'inLibrary': False, 'feedbackTokens': {'add':None, 'remove': None}, 'videoId': 'id', 'videoType': 'type', 'duration':'duration', 'year': year, 'artists': [{'name: 'name', 'id': id'}], 'duration_seconds': sec, 'views': 'views', 'isExplicit': Bool, 'thumbnails': [{'url': 'url', 'width': 60, 'height': 60}, {'url': 'url'}]
    try:
        song_list = []
        # for each result
        for song in results:
            song_object = Song(song['title'], extract_artists(song['artists']), time_to_seconds(song['duration']))  # create song object
            song_list.append(song_object)  # append to the list of songs
        return song_list
    except Exception:
        raise

# DO NOT MODIFY
def print_song_results(results):
    """
    Input: List containing "Song" objects
    Returns: None
    Working:
    This function is reponsible for printing the song results with a serial number beside them.
    """
    assert type(results[0]) == Song, "The list to be printed doesn't have the items of type 'Song'"

    print("RESULTS:")
    for i in range(len(results)):
        print(f"{i+1}. {results[i]}")

def search():
    """
    Input: None
    Return: A Song object representing the song the user wants to add into the Queue, or None if the user wants to go back
    Working:
    1. This function takes search query from the user
    2. Searches for the song using songSearch function
    3. Filters the information using filterInfo function
    4. Prints the song results using printSongResults function
    5. Asks for user choice
    6. Returns the chosen song information
    7. If the user wants to go back, it returns None
    """
    # 1 Takes Search Query
    query = input("Search: ")

    # 2 Searches for the song using songSearch function
    results = song_search(query)

    # 3 Filters the information using filterInfo function
    results = filter_info(results)

    # 4 Print the song results using printSongResults function
    print_song_results(results)

    # 5 asks for user choice
    print("")
    choice = input("Choose one of the following options:\n"
        "       Enter a number (1-5) to add a song to the playlist\n"
        "       Enter '0' to search again\n"
        "       Enter 'q' to go back\n"
        ">> ")
    while choice not in ['1', '2', '3', '4', '5', '0', 'q']:
        print('Invalid Input.')
        choice = input(">> ")
    # Returns the given song information

    # search again
    if choice == '0':
        return search()
    # return to menu
    elif choice == 'q':
        return None
    else:
        # return choice
        return results[int(choice)-1]

# DO NOT MODIFY
def main():
    """
    Drive Function
    """
    queue = MusicQueue()
    clear()
    print("WELCOME\n")
    choice_str = """Choose one of the following options:
                    \t1. Add Song
                    \t2. Next Song
                    \t3. Show Queue
                    \t4. Clear Queue
                    \t5. Quit
                    \tEnter the choice (eg: 2)
                """
    contBuild = True
    try:
        while contBuild:

            print('Currently playing:')
            if queue.is_empty() == False: 
                print('  ',queue.peek(),'\n')
            else: 
                print('  ',"None",'\n')

            print(choice_str)
            choice = input('>> ')
            while choice not in ['1','2','3','4','5']:
                print('Invalid Input.')
                choice = input('>> ')
            
            if choice == '1':
                song = search()
                if song != None:
                    if queue.is_empty():
                        queue.enqueue_b(song)
                    else:
                        place = input("Where would you like to add the song:\n\t1. Top\n\t2. End\n>> ")
                        while place not in ['1','2']:
                            print('Invalid Input.')
                            place = input('>> ')
                        
                        if place == '1':
                            queue.enqueue_f(song)
                        elif place == '2':
                            queue.enqueue_b(song)
                    print("Song added successfully!")
                    input("\nPress enter key to continue...")

            elif choice == '2':
                clear()
                queue.dequeue()
                print('Now playing:')
                if queue.size() > 0:
                    print("  ",queue.peek())
                else:
                    print("   None")
                input("\nPress enter key to continue...")

            elif choice == '3':
                clear()
                try:
                    print(queue)
                    input("\nPress enter key to continue...")
                except Exception as e:
                    print(e)
            
            elif choice == '4':
                clear()
                queue.clear()
                print('The queue has been cleared!')
                input("\nPress enter key to continue...")

            elif choice == '5':
                contBuild = False
            
            clear()

    except Exception as e:
        print(e)

    print("Thanks for listening!")

if __name__ == "__main__":
    main()