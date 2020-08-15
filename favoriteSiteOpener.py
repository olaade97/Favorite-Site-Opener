# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
#! python3
import webbrowser, sys, pyperclip


# Get address from command line.
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    
else: 
    # Get address from clipboard.
    website = pyperclip.paste()
    webbrowser.open(website)
    
#Opens the following links in your browswer
webbrowser.open('https://www.reddit.com/r/frugalmalefashion/')
webbrowser.open('https://www.reddit.com/r/consoledeals/')
webbrowser.open('https://www.reddit.com/r/SneakerDeals/')

# TODO: Get address from clipboard.
