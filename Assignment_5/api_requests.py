# A program to make API requests to the usefuless facts API
# and display the results based on user input

import requests
import json

base_url = 'https://uselessfacts.jsph.pl/api/v2/facts/'
query = input(f"Type 'random' for a random useless fact or 'today' or today's usefuless fact: ")

try:
    query = query.lower()
    if query == 'random':
        query = 'random'
    elif query == 'today':
        query = 'today'
    else:
        print("Invalid input. Please try again.")
        exit()
except:
    exit()

r = requests.get(f'{base_url}{query}')

try:
    r.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f'An error occurred: {e}')
    exit() 
# requests.status_codes = 200
# 200 is the status code for a successful HTTP request
# 404 is the status code for a failed HTTP request
# 500 is the status code for a server error

fact = r.json()['text']
fact_id = r.json()['id']
source = r.json()['source']
source_url = r.json()['source_url']
permalink = r.json()['permalink']
# language = r.json()['language']

print(f'Useless fact: {fact}')
print(f'Fact ID: {fact_id}')
print(f'Source: {source}')
print(f'Source URL: {source_url}')
print(f'Permalink: {permalink}')
# print(f'Language: {language}')