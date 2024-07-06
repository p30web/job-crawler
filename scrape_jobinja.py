import os
import django
import requests
from bs4 import BeautifulSoup

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobcrawler.settings')
django.setup()

from company.models import Company, CompanyCategory
from location.models import Location


def scrape_jobinja():
    url = 'https://jobinja.ir/companies/nik-dade-pardaz/jobs/ASjM/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-laravel-back-end-developer-%D8%AF%D8%B1-%D9%86%DB%8C%DA%A9-%D8%AF%D8%A7%D8%AF%D9%87-%D9%BE%D8%B1%D8%AF%D8%A7%D8%B2?_ref=16'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data (adjust selectors based on actual HTML structure)

    # Extract data
    header = soup.find('h2', {'class': 'c-companyHeader__name'}).text.strip()
    name_fa, name_en = header.split('|')
    name_fa = name_fa.strip()
    name_en = name_en.strip()

    # Extract category, size, and website
    meta_items = soup.find('div', {'class': 'c-companyHeader__meta'}).find_all('span',
                                                                               {'class': 'c-companyHeader__metaItem'})
    category_name = meta_items[0].find('a').text.strip()
    size = meta_items[1].text.strip()
    website = meta_items[2].find('a')['href']

    # Extract established year (if available)
    established_year_tag = soup.find('div', {'class': 'established-year'})
    established_year = int(established_year_tag.text.strip()) if established_year_tag else None

    # Extract city name (if available)
    city_name_tag = soup.find('div', {'class': 'city-name'})
    city_name = city_name_tag.text.strip() if city_name_tag else None

    # Get or create category
    category, created = CompanyCategory.objects.get_or_create(name=category_name)

    # Get or create location (if city name is available)
    location = None
    if city_name:
        location, created = Location.objects.get_or_create(city_name=city_name)

    # Get or create company
    company, created = Company.objects.get_or_create(
        name_fa=name_fa,
        name_en=name_en,
        category=category,
        size=size,
        website=website,
        established_year=established_year,
        location=location
    )


if __name__ == '__main__':
    scrape_jobinja()
