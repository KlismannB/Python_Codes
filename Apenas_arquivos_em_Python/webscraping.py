import json
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from matplotlib import pyplot as plt

# 1 - Get the HTML webpage content using the URL and the selenium driver
url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"
top_10_ranking = {}

rankings = {
  '3points': {'field' : 'FG3M', 'label' : '3PM'},
  'points': {'field' : 'PTS', 'label' : 'PTS'},
  'assistants': {'field' : 'AST', 'label' : 'AST'},
  'rebounds' : {'field' : 'REB', 'label' : 'REB'},
  'steals' : {'field' : 'STL', 'label' : 'STL'},
  'blocks' : {'field' : 'BLK', 'label' : 'BLK'},
}

def buildrank(type):
      
    field = rankings[type]['field']
    label = rankings[type]['label']
    
    driver = webdriver.Firefox()

    driver.get(url)
    time.sleep(10)  

    driver.find_element_by_xpath(
      "//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='{}']".format(field)).click()

    element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
    html_content = element.get_attribute('outerHTML')

    # print(html_content)

    # 2 - Parse the HTML content -BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')

    # 3 - Structure the content in a DataFrame- Pandas
    df_full = pd.read_html(str(table))[0].head(10)
    df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', label]]
    df.columns = ['pos', 'player', 'team', 'total']

    # print(df)

    driver.quit()

    # 4 - Transform the data into a dictionary of their own data
    return df.to_dict('records')

for k in rankings:
      top_10_ranking[k] = buildrank(k)
      print (k)
      plt.title('Categoria Avaliativa: ' + k)
      plt.ylabel('Jogador')
      plt.xlabel('Pontos')
      plt.show()

# 5 - Convert and save into a JSON file
js = json.dumps(top_10_ranking)
fp = open('ranking.json', 'w')
fp.write(js)
fp.close()



# ----- PRE-INSTALL ----- #
'''
  * pip install requests2
  * pip install pandas
  * pip install lxml
  * pip install beautifulsoup4
  * pip install selenium
'''
