from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def index(request):
    my_lovely_list = ['foo', 'bar', 'baz', 'boop']
    context = {'my_lovely_list': retrieve_calendar_data()}
    return render(request, 'greengrocer_calendar_app/index.html', context)


def retrieve_calendar_data():
    url = "https://realpython.github.io/fake-jobs/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    job_elements = results.find_all("div", class_="card-content")
    job_list = []

    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        job_list.append((title_element.text.strip(), company_element.text.strip(), location_element.text.strip()))

    return job_list
