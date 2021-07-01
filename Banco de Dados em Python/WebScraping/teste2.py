import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

res = requests.get("http://www.nationmaster.com/country-info/stats/Media/Internet-users")

soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0]

# print(table)

df = pd.read_html(str(table))

# print(df) 

#convertendo tabela em formato json
# print(df[0].to_json(orient='records'))

#imprimindo numa tabela
print(tabulate(df[0],headers='keys',tablefmt='psql'))