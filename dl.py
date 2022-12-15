import os, fnmatch
import urllib.request
import re

def getCWD():
    return os.getcwd()

def getUrl(file):
    data = urllib.request.urlopen(file)
    contents = data.read().decode('utf-8')
    
    if(re.findall('(https?://\S+)', contents)):
        return re.findall('(https?://\S+)', contents)[0]
    return False

# find a single file
def findFile(pattern, path):
    result = []

    for root, dir, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

# find all files in
def findAll(name, path):
    result = []
    for root, dir, files in os.walk(path):
        if(name in files):
            result.append(os.path.join(root, name))
    return result

def shellquote(item):
    if not item:
        return "''"
    # Pre-escape any escape characters                                                                                                                    
    item = item.replace('\\', r'\\')
    if "'" not in item:
        # Contains no single quotes, so we can                                                                                                        
        # single-quote the output.                                                                                                                    
        return f"'{item}'"
    else:
        # Enclose in double quotes. We must escape                                                                                                    
        # "$" and "!", which which normally trigger                                                                                                   
        # expansion in double-quoted strings in shells.                                                                                               
        # If it contains double quotes, escape them, also.                                                                                               
        item = item.replace(r'$', r'\$') \
                   .replace(r'!', r'\!') \
                   .replace(r'"', r'\"')
        return f'"{item}"'

files = findFile('*.webloc', getCWD())

if(files):
    for file in files:
        url = getUrl(file)
        if(url):
            os.system("/opt/homebrew/bin/yt-dlp "+shellquote(url))
else:
    print('file not found')
