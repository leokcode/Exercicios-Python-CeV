import requests
url = "https://www.pudim.com.br/"
try:
    response = requests.get(url, timeout=5)
    print('\033[0;32mConsegui acessar o site pudim com sucesso.\033[m')
except:
    print('\033[0;31mO site pudim não está mais acessível no momento.\033[m')
