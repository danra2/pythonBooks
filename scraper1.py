import requests, bs4

res = requests.get('http://nostarch.com')
#User requests.get() to download the main page from the no starch press website, and then passes the text attribute of the response to bs4.BeautifulSoup()
#The Object then returned is stored into the variable noStarchSoup
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)
