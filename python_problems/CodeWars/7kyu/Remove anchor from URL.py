'''Complete the function/method so that it returns the url with anything after the anchor (#) removed.

Examples
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"'''

from urllib.parse import urlparse

def remove_url_anchor(url):

    return urlparse(url)._replace(fragment='').geturl()



