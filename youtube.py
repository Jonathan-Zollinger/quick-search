# this program is designed for users to search youtube from the run box. it will allow the user
#	to run the search off their clipboard or to type in a new search. this requires a batch file
#	in a folder on the PATH environment to point to this file

import webbrowser, sys, pyperclip

# allow this to run from the command line
sys.argv

# give the base website URL
website = "https://www.youtube.com/results?search_query="#<search> goes here

#if there's only one command, we know the user is looking to use their clipboard as their search
#	otherwise, we know the command line also contains the search.
if len(sys.argv) > 1:
	#combine the rest of the command line arguments into one string
	#	(fyi, spaces in the run box start a new command)
	search = ' '.join(sys.argv[1:])
else:
	search = pyperclip.paste()

webbrowser.open(website+search)