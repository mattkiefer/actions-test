import requests

response = requests.get('https://northwestern.edu')
outfile = open('nu.html','w')
outfile.write(response.content)
outfile.close()
