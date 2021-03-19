# Sanfoundry Scrapper

A python scrapper script that scrappes all the questions and answers from a sanfoundry page following all `next` links.

## Requirements

- BeautifulSoup (bs4)
- Requests (requests)

> Note: You must already have python installed.

### Install Requirements

```bash
> pip install -r requirements.txt
```

## Scrape Questions

### Run `scrapper.py`

```bash
> python scrapper.py
```

### Enter Sanfoundry page `url`

(e.g <https://www.sanfoundry.com/software-engg-mcqs-software-engineering-ethics-1/>)

```bash
PS C:\Users\USER\Sanfoundry Scrapper>python scrapper.py
Enter the sanfoundry url of the page  
at the begginning of the questions >> https://www.sanfoundry.com/software-engg-mcqs-software-engineering-ethics-1/
```

## Search Questions

### Run `search.py`

```bash
> python search.py
```

### Enter question to search

(e.g **Identify dilemma from situations mentioned**)

```bash
PS C:\Users\USER\Sanfoundry Scrapper> python search.py

With 1000 questions to search from.
CTRL + C to exit.

Paste question >> Identify dilemma from situations mentioned

Best Match:
Question 4. Identify an ethical dilemma from the situations mentioned below:
a) Your employer releases a safety-critical system without finishing the testing of the system
b) Refusing to undertake a project
c) Agreement in principle with the policies of senior management
d) All of the mentioned

 Answer: a
Explanation: None.

Paste question >> |
```
