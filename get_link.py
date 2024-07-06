import requests
from bs4 import BeautifulSoup


def get_job_links(url):
    # ارسال درخواست به صفحه مورد نظر
    response = requests.get(url)
    # بررسی وضعیت پاسخ
    if response.status_code != 200:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return []

    # پارس کردن محتوای HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # پیدا کردن لیست مشاغل
    job_list = soup.find('ul', class_='o-listView__list c-jobListView__list')
    if not job_list:
        print("Job list not found.")
        return []

    # استخراج لینک‌های شغلی
    job_links = job_list.find_all('a', class_='c-jobListView__titleLink')

    # استخراج href هر لینک
    links = [a['href'] for a in job_links if 'href' in a.attrs]
    return links


def save_links_to_file(links, filename):
    # نوشتن لینک‌ها در فایل متنی
    with open(filename, 'w') as file:
        for link in links:
            file.write(link + '\n')
    print(f"Links saved to {filename}")


# لینک مورد نظر شما
url = "https://jobinja.ir/jobs?filters%5Bkeywords%5D%5B%5D=laravel&filters%5Blocations%5D%5B%5D=&filters%5Bjob_categories%5D%5B%5D=&b="

# استخراج لینک‌ها
job_links = get_job_links(url)

# ذخیره لینک‌ها در فایل متنی
save_links_to_file(job_links, 'job_links.txt')
