# =================================================================
# CMPUT 175 - Introduction to the Foundations of Computation II
# Lab 6 - Advanced Music Queue
#
# ~ Created by CMPUT 175 Team ~
# edited by Alice Cai 2026-03-10
# ============================================================


# A music player that searches Youtube, adds songs, plays next, displays queue.
# To run from terminal: python "C:\Users\Alice C\PycharmProjects\CMPUT-175\lab6\advanced_music_queue.py"

# Install ytmusicapi using pip
from ytmusicapi import YTMusic
from structures import DLinkedListNode, DLinkedList, Song, time_to_seconds
import os

NO_OF_RESULTS = 5

# DO NOT MODIFY
def clear():
    '''
    Clears the screen based on the operating system.
    '''
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')

def extract_artists(song):
    """
    Input: song, A dictionary containing song information
    Returns: A string of artist names separated by commas
    Working:
    This function extracts and returns a comma-separated string of artist names from the song dictionary.
    """
    try:
        artists = ""
        # if o artist information is available (empty list)
        if len(song) == 0:
            return "NA"
        # for each artist in the list
        for name in song:
            artists += name['name'] + ", "  # concatenate with comma seperator
        return artists[0:len(artists)-2]  # cut off last comma and space
    # Error occurred
    except:
        raise Exception("Artist error")
def song_search(query):
    """
    Input: Search query
    Returns: Top "NO_OF_RESULTS" i.e. 5 results from the retrieved data
    Working:
    This function invokes the search method on YTMusic object with required arguments
    """
    # create YT music object
    yt_music = YTMusic()
    return yt_music.search(query, filter="songs", scope=None)[0:NO_OF_RESULTS]  # top X results

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
            song_object = Song(song['title'], extract_artists(song['artists']),
                               time_to_seconds(song['duration']))  # create song object
            song_list.append(song_object)  # append to the list of songs
        return song_list
    except Exception:
        raise

# DO NOT MODIFY
def print_song_results(results):
    """
    Input: A list of Song objects
    Returns: None
    Working:
    This function prints the list of Song objects in a formatted manner.
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
    2. Searches for the song using song_search function
    3. Filters the information using filter_info function
    4. Prints the song results using print_song_results function
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
        return results[int(choice) - 1]

def main():
    """
    Initializes the music queue and provides an interactive menu to manage songs.
    Users can add songs, navigate to next or previous songs, remove the current song,
    display or clear the queue, and quit the program.

    NOTE: You need to modify the main function to use the DLinkedList class to manage the music queue. 
          Add the new features that are needed for this Lab assignment as per the description.

          ** MAKE SURE YOU READ THE DESCRIPTION CAREFULLY AND UNDERSTAND THE REQUIREMENTS. **
    """
    queue = DLinkedList()
    clear()
    print("WELCOME\n")
    choice_str = """Choose one of the following options:
                \t1. Add Song
                \t2. Next Song
                \t3. Previous Song
                \t4. Remove Current Song
                \t5. Show Queue
                \t6. Clear Queue
                \t7. Quit
                Enter the choice (eg: 2)
                """
    contBuild = True
    try:
        while contBuild:

            # Currently Playing Display
            print('Currently playing:')
            if queue.is_empty() == False: 
                print('  ',queue.get_current(),'\n')  # changed peek() to get_current()
            else: 
                print('  ',"None",'\n')

            # Main Menu
            print(choice_str)
            choice = input('>> ')
            while choice not in ['1','2','3','4','5', '6', '7']:
                print('Invalid Input.')
                choice = input('>> ')

            # Choice 1: Add Song
            if choice == '1':
                # search for the song
                song = search()
                if song != None:
                    # if the queue is empty add to the end
                    if queue.is_empty():
                        queue.add_last(song)  # changed enqueueB to add_last
                    # list is not empty, add next or add to the end
                    else:
                        place = input("Where would you like to add the song:\n\t1. Add Next\n\t2. Add to the End\n>> ")
                        while place not in ['1','2']:
                            print('Invalid Input.')
                            place = input('>> ')

                        # Add next
                        if place == '1':
                            queue.add_next(song)  # changed enqueueF to add_next()
                        # Add last
                        elif place == '2':
                            queue.add_last(song)  # changed enqueueB to add_last()
                    print("Song added successfully!")
                    input("\nPress enter key to continue...")

            # Choice 2: Next Song
            elif choice == '2':
                clear()
                is_queue_empty = queue.play_next()  # changed dequeue to play_next()

                # if no song ahead
                if not is_queue_empty:
                    print('No Songs ahead in queue.')
                else:
                    # print the new current song
                    print('Now playing:', queue.get_current().get_name())
                input("\nPress enter key to continue...")

            # Choice 3: Previous Song
            elif choice == '3':
                clear()
                is_queue_empty = queue.play_previous()  # changed dequeue to play_previous()

                # if no song behind
                if not is_queue_empty:
                    print('No Songs behind in queue.')
                else:
                    # print the new current song
                    print('Now playing:', queue.get_current().get_name())
                input("\nPress enter key to continue...")

            # Choice 4: Remove current song
            elif choice == '4':
                clear()
                current_song = queue.remove_current()  # changed dequeue to remove_current()
                print(f"'{current_song.get_name()}' removed successfully!")
                input("\nPress enter key to continue...")

            # Choice 5: Show Queue
            elif choice == '5':
                clear()
                try:
                    print(queue)
                    input("\nPress enter key to continue...")
                except Exception as e:
                    print(e)

            # choice 6: Clear Queue
            elif choice == '6':
                clear()
                queue.clear()
                print('The queue has been cleared!')
                input("\nPress enter key to continue...")

            # choice 7: Quit
            elif choice == '7':
                contBuild = False
            
            clear()

    except Exception as e:
        print(e)

    print("Thanks for listening!")

if __name__ == "__main__":
    main()