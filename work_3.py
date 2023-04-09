import urllib.request

url = 'https://www.python.org'
response = urllib.request.urlopen(url)
html_code = response.read().decode()

char_count = {}
for char in html_code:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

f=open("readme.md","w")
for char in char_count:
    f.write(f"{char}:{char_count[char]}"+"\n")
f.close()