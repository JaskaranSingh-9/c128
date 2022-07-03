from bs4 import BeautifulSoup
import requests
import pandas as pd
import time,csv
from selenium.webdriver.common.by import By
START_URL =  "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(START_URL)
soup = BeautifulSoup(page.text, "html.parser")
temp_list = []
plant_data=[]
star_table=soup.find_all("table")
star_row=star_table[7].find_all("tr")
headers=["name","light_years_from_earth","Radius","steler_magnitude","discovery_date"]
for tr_tag in soup.find_all("td",attrs={"class","Field_brown_dwarfs"}):
            tr_tags=tr_tag.find_all("td")
            temp_list=[]
            row = [i.text.rstrip() for i in tr_tag] 
            temp_list.append(row)
            for index,tr_tag in enumerate(tr_tags):
                if index==0:
                    temp_list.append(tr_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append("")
            plant_data.append(temp_list)
            page.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[8]/thead/tr').click()
with open("scrapper2.csv","w") as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(star_row)
        csvwriter.writerows(plant_data)

