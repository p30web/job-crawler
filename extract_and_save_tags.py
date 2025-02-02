import os
import django
import re
import requests
from urllib.parse import urlparse, unquote
from bs4 import BeautifulSoup

# تنظیمات جنگو
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobcrawler.settings')
django.setup()

from job_tags.models import JobTag

job_links = [
"https://jobinja.ir/companies/nafw/jobs/AInJ/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3-laravel-%D8%AF%D8%B1-%D9%86%D9%88%DB%8C%D9%86-%D8%A2%D9%88%D8%A7%D8%B2%D9%87-%DA%AF%D8%B1%D8%A7%D9%86-%D9%81%D8%B1%D8%A7-%D9%88%D8%A8?_ref=16",
"https://jobinja.ir/companies/fanavaran-zehn-rasa/jobs/AsKC/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3-php-laravel-%D8%AF%D8%B1-%D9%81%D9%86%D8%A7%D9%88%D8%B1%D8%A7%D9%86-%D8%B0%D9%87%D9%86-%D8%B1%D8%B3%D8%A7?_ref=16",
"https://jobinja.ir/companies/my-siloo/jobs/AfpS/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3-php-laravel-%D8%AF%D8%B1-%D9%85%D8%A7%DB%8C-%D8%B3%DB%8C%D9%84%D9%88?_ref=16",
"https://jobinja.ir/companies/itechnet/jobs/AzVv/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-remote-laravel-devops-engineer-%D8%AF%D8%B1-%D8%A2%DB%8C%D8%AA-%DA%A9-%D9%86-%D8%AA?_ref=16",
"https://jobinja.ir/companies/banirayanpardazno/jobs/AsQx/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-senior-php-developer-laravel-%D8%AF%D8%B1-%D8%A8%D8%A7%D9%86%DB%8C-%D8%B1%D8%A7%DB%8C%D8%A7%D9%86-%D9%BE%D8%B1%D8%AF%D8%A7%D8%B2-%D9%86%D9%88?_ref=16",
"https://jobinja.ir/companies/iraninvr/jobs/A0XO/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3-php-laravel-%D8%AF%D8%B1-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D8%AF%D8%B1-%D9%88%D8%A7%D9%82%D8%B9%DB%8C%D8%AA-%D9%85%D8%AC%D8%A7%D8%B2%DB%8C?_ref=16",
"https://jobinja.ir/companies/mehromah/jobs/AJJ0/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3-php-laravel-%D8%AF%D8%B1-%D9%85%D9%87%D8%B1%D9%88%D9%85%D8%A7%D9%87?_ref=16",
"https://jobinja.ir/companies/nik-dade-pardaz/jobs/ASjM/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-laravel-back-end-developer-%D8%AF%D8%B1-%D9%86%DB%8C%DA%A9-%D8%AF%D8%A7%D8%AF%D9%87-%D9%BE%D8%B1%D8%AF%D8%A7%D8%B2?_ref=16",
"https://jobinja.ir/companies/chitasoft/jobs/AAQv/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-back-end-developer-laravel-%D8%AF%D8%B1-%D8%B3%D8%B1%D9%85%D8%A7%DB%8C%DA%A9%D8%B3?_ref=16",
"https://jobinja.ir/companies/clever-2/jobs/AbXi/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3-laravel-%D9%85%D8%B4%D9%87%D8%AF-%D8%AF%D8%B1-%DA%A9%D9%84%D9%88%D8%B1?_ref=16",
"https://jobinja.ir/companies/sepanta-9/jobs/A915/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3-laravel-%D8%AF%D9%88%D8%B1%DA%A9%D8%A7%D8%B1%DB%8C-%D8%AF%D8%B1-%D8%AA%D9%88%D8%B3%D8%B9%D9%87-%D9%81%D9%86%D8%A7%D9%88%D8%B1%DB%8C-%D8%A7%D8%A8%D8%B1%DB%8C-%D8%B3%D9%BE%D9%86%D8%AA%D8%A7?_ref=16",
"https://jobinja.ir/companies/mailerever-1/jobs/AbrQ/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3-%D8%A7%D8%B5%D9%81%D9%87%D8%A7%D9%86-php-laravel-%D8%AF%D8%B1-%D9%86%DA%AF%D8%A7%D8%B1-%D9%BE%D8%B1%D8%AF%D8%A7%D8%B2%D8%B4?_ref=16",
"https://jobinja.ir/companies/uxegroup/jobs/AbwR/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3-php-%D8%A7%D8%B5%D9%81%D9%87%D8%A7%D9%86-laravel-%D8%AF%D8%B1-%D8%AA%D8%AC%D8%B1%D8%A8%D9%87-%D8%B3%D8%A7%D8%B2%D8%A7%D9%86-%D8%AE%D9%84%D8%A7%D9%82?_ref=16",
"https://jobinja.ir/companies/sakhtbazar/jobs/B9V/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3-laravel-php-%D8%AA%D8%A8%D8%B1%DB%8C%D8%B2-%D8%AF%D8%B1-%D8%B3%D8%A7%D8%AE%D8%AA-%D8%A8%D8%A7%D8%B2%D8%A7%D8%B1?_ref=16",
"https://jobinja.ir/companies/ulduz-persian-technologists/jobs/Af7x/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3-php-%D8%B4%DB%8C%D8%B1%D8%A7%D8%B2-laravel-%D8%AF%D8%B1-%D9%81%D9%86-%D8%A2%D9%88%D8%B1%D8%A7%D9%86-%D9%BE%D8%B1%D8%B4%DB%8C%D9%86-%D8%A7%D9%88%D9%84%D8%AF%D9%88%D8%B2?_ref=16",
"https://jobinja.ir/companies/directam/jobs/AWag/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%DA%A9%D8%A7%D8%B1%D8%A2%D9%85%D9%88%D8%B2-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3-laravel-php-%D8%AF%D8%B1-%D8%AF%D8%A7%DB%8C%D8%B1%DA%A9%D8%AA%D9%85?_ref=16",
"https://jobinja.ir/companies/Avin%20Media/jobs/AfNM/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3-laravel-php-%D8%AF%D9%88%D8%B1%DA%A9%D8%A7%D8%B1%DB%8C-%D8%AF%D8%B1-%D8%A2%D9%88%DB%8C%D9%86-%D9%85%D8%AF%DB%8C%D8%A7?_ref=16",
"https://jobinja.ir/companies/directam/jobs/Abfw/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3-php-laravel-%D8%A7%D8%B5%D9%81%D9%87%D8%A7%D9%86-%D8%AF%D8%B1-%D8%AF%D8%A7%DB%8C%D8%B1%DA%A9%D8%AA%D9%85?_ref=16",
"https://jobinja.ir/companies/irapardaz/jobs/A05l/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-back-end-developer-php-laravel-%D8%AF%D8%B1-%D8%A7%DB%8C%D8%B1%D8%A7%D9%BE%D8%B1%D8%AF%D8%A7%D8%B2?_ref=16",
"https://jobinja.ir/companies/entekhab-industrial-group/jobs/AHF2/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%DA%A9%D8%A7%D8%B1%D8%B4%D9%86%D8%A7%D8%B3-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3%DB%8C-laravel-%D8%A7%D8%B5%D9%81%D9%87%D8%A7%D9%86-%D8%AF%D8%B1-%DA%AF%D8%B1%D9%88%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%A7%D9%86%D8%AA%D8%AE%D8%A7%D8%A8-%D8%A7%D9%84%DA%A9%D8%AA%D8%B1%D9%88%D9%86%DB%8C%DA%A9?_ref=16",
]

def extract_english_words(text):
    # Find all English words
    english_words = re.findall(r'[a-zA-Z]+', text)
    return english_words

def save_words_to_db(words):
    for word in words:
        # Check if the word already exists in the database
        if not JobTag.objects.filter(name=word).exists():
            # Save the word to the database
            JobTag.objects.create(name=word)

def main():
    for url in job_links:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            job_view = soup.find(class_='c-jobView')
            if job_view:
                text = job_view.get_text()
                english_words = extract_english_words(text)
                save_words_to_db(english_words)
        else:
            print(f"Failed to retrieve the page: {url}")

if __name__ == '__main__':
    main()
