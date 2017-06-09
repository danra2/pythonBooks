import requests
#This program essentially is used to download a specifc file from a specific webpage.
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
# <class 'requests.models.Response'>
# res.status_code == requests.codes.ok
#res.raise_for_status()
#Is the better method for raising errors or knowing whether or not something was successful as opposed to res.status_code.
#The status code for okay is HTTP 200 protocol, much like the 404 for not found.
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
#Always do this status, following the .get method, because you want to know that you successfully downloaded the file in the first place.

len(res.text)
print(res.text[:250])
