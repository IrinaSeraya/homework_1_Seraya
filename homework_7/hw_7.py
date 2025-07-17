import csv
import requests
import time
import json
import functools
import re
import os
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/"

def wiki_page_dl(country):
   responce = requests.get(URL + country, timeout=1)
   responce.raise_for_status()
   return responce.text

def data_caching(func):
   @functools.wraps(func)
   def wrapper(*args, **kwargs):
        if os.path.exists("countries_data_cache.json"):
            with open("countries_data_cache.json") as fh:
                countries_data_cache = json.loads(fh.read())
        else:
            countries_data_cache = dict()
        country = args[0]
        if country not in countries_data_cache:
            res = func(*args, **kwargs)
            if res is not None:
                countries_data_cache[country] = [res[1], res[2], res[3]]
                with open("countries_data_cache.json", "w") as fh:
                    json.dump(countries_data_cache, fh, indent="    ")
        else:
            res = [
                country,
                countries_data_cache[country][0],
                countries_data_cache[country][1],
                countries_data_cache[country][2],
            ]
        return res
   return wrapper

@data_caching
def parse_web_page(country):
    web_page = wiki_page_dl(country)

    if web_page is None:
        return None
    
    capital = (
        BeautifulSoup(web_page, "lxml")
        .find(string=re.compile("Capital"))
        .find_next("td")
        .find("a")
        .text
    )

    area = (
        BeautifulSoup(web_page, "lxml")
        .find("a", string=re.compile("Area"))
        .find_next("td")
        .text.replace(",", "")
    )

    population =(
        BeautifulSoup(web_page, "lxml")
        .find(string=re.compile("Estimate"))
        #.find_next("td")
        #.text.strip()
        #.text.replace(",", "")
    )

    result = [country, capital, area, population]

    return result

def main():
    input_file = "countries.txt"
    while True:
        user_input = input(
            f"Введите название исходного файла"
            f" или нажмите Enter, чтобы использовать файл по умолчанию (countries.txt)")
        if user_input == "":
            break
        else:
            if os.path.exists(user_input):
                input_file = user_input
                break
            else:
                print("Файл не найден")
                break

    with open(input_file) as fh:
        countries = fh.read().splitlines()

    data = [["country", "capital", "area", "population"]]

    for country in countries:
        new_row = parse_web_page(country)
        if new_row is not None:
            data.append(new_row)
    
    output_file = "countries_data.csv"

    while True:
        user_input = input(
            f"Введите название файла для сохранения информации" 
            f' или нажмите Enter для использования названия по умолчанию "{output_file}"')
        if user_input == "":
            break
        else:
            output_file = user_input
            break

    with open(output_file, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(data)
    
    print("Иформация по запрашиваемым сранам сохранена в файле '{output_file}'")

main()
 