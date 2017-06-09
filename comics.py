#Download the pages with the requests module.
#Find the URL of the comic image for a page using Beautiful Soup.
#Downlaod and save the comic image to the hard drive with iter_content().
#Find the URL of the prevous comic link, and repeat.

#Python 3
# comics.py Downloads every single XKCD comic.

import requests, os, bs4

url = 'http://xkcd.com' # starting url
os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd

while not url.endswith('#'):
    # TODO: Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # TODO: Download the image.
    #Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
    #Download the image.
    print('Downloading image %s...' %(comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()
    # TODO: Save the image to./xkcd.
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(1000000):
        imageFile.write(chunk)
    imageFile.close()
    # TODO: Get the Prev Button's URL.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
