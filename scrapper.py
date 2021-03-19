import re
import json
from bs4 import BeautifulSoup as soup
import requests as req

HTML_PARSE_FORMAT = 'html.parser'
JSON_FILE = 'questions.json'

try:
    with open(JSON_FILE) as f:
        question_data: dict = json.load(f)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    print('Creating questions.json')
    with open(JSON_FILE, 'w') as f:
        json.dump({"questions": []}, f)
    with open(JSON_FILE) as f:
        question_data: dict = json.load(f)


def scrappe(starting_url):

    next_url = starting_url

    while next_url != None:
        try:
            print(f'Scrapping data from {next_url}')

            html = req.get(next_url).text
            _soup = soup(html, HTML_PARSE_FORMAT)

            main_content = [x for x in _soup.find(
                "div", {"class": "entry-content"}).findAll('p') if re.search(r'\d\. .*', x.text)][0]

            split_content = ['<p>' + x for x in str(main_content).split('<p>')]

            for x in split_content:
                if re.search(r'<span', x):
                    question_data["questions"].append(
                        {
                            "q": soup(x.split('<span')[0], HTML_PARSE_FORMAT).find('p').text,
                            "a": soup(x.split('<span')[1], HTML_PARSE_FORMAT).find('div').text
                        }
                    )

            next_url = _soup.find("a", {"rel": "next"})['href']
        except:
            print('ERROR')
            next_url = None

    with open(JSON_FILE, 'w') as f:
        json.dump(question_data, f)

    print(
        f'Your questions.json has {len(question_data["questions"])} questions')


scrappe(input('Enter the sanfoundry url of the page\nat the begginning of the questions >> '))
