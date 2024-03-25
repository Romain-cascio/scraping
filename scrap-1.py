import requests
import pandas as pd
import os
import json
import time
import csv
import random
from io import StringIO
from fp.fp import FreeProxy
from bs4 import BeautifulSoup

# simple request on webpage
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page
print(page.content)

#formating 
page.text.split("\n")

# Attempt to read from a file
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    # If the file does not exist, create it and write a default message
    with open('example.txt', 'w') as file:
        file.write("This is a new file.")
        print("File 'example.txt' was not found and has been created.")

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

#list all files in a directory
for file in os.listdir('/Users/romaincascio/Documents/H3Hitema/python/web_scrap/'):
    print(file)

with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

data = [
    {
        "name": "Alice Brown",
        "department": "Marketing",
        "salary": 70000
    },
    {
        "name": "Bob Smith",
        "department": "Sales",
        "salary": 65000
    },
    {
        "name": "Carol Jones",
        "department": "IT",
        "salary": 75000
    }
]

#write this variable inside a json file
with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)

#then read the data
with open('output.json', 'r') as file:
    data = json.load(file)
    print(data)

def csv_reader(file_content):
    return csv.reader(StringIO(file_content))

# Fetch the file content from the URL
url = 'https://gist.githubusercontent.com/bdallard/d4a3e247e8a739a329fd518c0860f8a8/raw/82fb43adc5ce022797a5df21eb06dd8e755145ea/data-json.csv'
response = requests.get(url)
file_content = response.text

tmp=0
start_time = time.time()
csv_data = csv_reader(file_content)
for row in csv_data:
    tmp+=int(row[0][-1]) #some dummy operation
end_time = time.time()

print("Traditional approach took:", end_time - start_time, "seconds")

def csv_reader_gen(file_content):
    for row in csv.reader(StringIO(file_content)):
        yield row

# Fetch the file content from the URL
url = "https://gist.githubusercontent.com/bdallard/d4a3e247e8a739a329fd518c0860f8a8/raw/82fb43adc5ce022797a5df21eb06dd8e755145ea/data-json.csv"
response = requests.get(url)
file_content = response.text

tmp=0
start_time = time.time()
csv_gen = csv_reader_gen(file_content)
for row in csv_gen:
    tmp+=int(row[0][-1]) #some dummy operation
end_time = time.time()

print("Generator approach took:", end_time - start_time, "seconds")

response = requests.get('http://httpbin.org/ip') 
#print(response.json()['origin']) #your personnal ip

proxy = FreeProxy(country_id=['FR']).get(); proxy

proxy_list = [FreeProxy(country_id=['FR']).get() for x in range(150)]; proxy_list

proxies = {'http': proxy_list[1]} 
response = requests.get('http://httpbin.org/ip', proxies=proxies) 
print(response.json()['origin']) # our proxy !!

response = requests.get('http://httpbin.org/headers') 
print(response.json()['headers'])
# python-requests/2.25.1

#!curl http://httpbin.org/headers
#try a custom user-agent
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 
response = requests.get('http://httpbin.org/headers', headers=headers) 
print(response.json()['headers']['User-Agent']) # Mozilla/5.0 ...

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (iPad; CPU OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/604.1.34 (KHTML, like Gecko) Edge/90.0.818.56',
    'Mozilla/5.0 (Linux; Android 10; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Mobile Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'
]

user_agent = random.choice(user_agents) 
headers = {'User-Agent': user_agent} 
response = requests.get('https://httpbin.org/headers', headers=headers) 
print(response.json()['headers']['User-Agent']) 
# Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) ...

headers_list = [
    {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Host": "httpbin.org",
        "Sec-Ch-Ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    },
    {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Host": "httpbin.org",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0"
    },
    {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Host": "httpbin.org",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    },
    {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en;q=0.5",
        "Host": "httpbin.org",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
    },
    {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Host": "httpbin.org",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15"
    }
]

headers = random.choice(headers_list) 
response = requests.get('https://httpbin.org/headers', headers=headers, proxies=proxies) 
print(response.json()['headers'])