import codecs
import os
from bs4 import BeautifulSoup

directory = "docs_old" 
todirectory = "docs"
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        path_from = os.path.join(directory, filename)
        path_to = os.path.join(todirectory, filename)
        
        # Read the HTML file with Windows-1252 encoding
        with codecs.open(path_from, 'r', 'windows-1252') as file:
            html_content = file.read()

        # Parse the HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the meta tag
        meta_tag = soup.find('meta', {'http-equiv': 'Content-Type'})

        # Update the charset attribute
        meta_tag['charset'] = 'utf-8'

        # Write the modified HTML with UTF-8 encoding
        with codecs.open(path_to, 'w', 'utf-8') as file:
            file.write(str(soup))
