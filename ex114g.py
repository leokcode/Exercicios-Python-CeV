import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[0;31mO site pudim não está mais acessível no momento.\033[m')
else:
    print('\033[0;32mConsegui acessar o site pudim com sucesso.\033[m')
    #print(site.read())
