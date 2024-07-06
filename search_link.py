import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import Counter


def get_job_description(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve job page. Status code: {response.status_code}")
        return ""

    soup = BeautifulSoup(response.content, 'html.parser')

    description = soup.find('div', class_='o-box__text')
    if not description:
        print("Job description not found.")
        return ""

    return description.get_text(strip=True)


def get_repeated_items(descriptions):
    all_text = ' '.join(descriptions)
    words = all_text.split()
    word_counts = Counter(words)
    repeated_items = {word: count for word, count in word_counts.items() if count > 1}
    return repeated_items



    # لینک‌های شغلی (این لیست را با لینک‌های واقعی خود تکمیل کنید)
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

# استخراج توضیحات شغلی
descriptions = [get_job_description(url) for url in job_links]

# ساخت DataFrame
df = pd.DataFrame({'url': job_links, 'description': descriptions})

# ذخیره DataFrame در فایل CSV
df.to_csv('job_descriptions.csv', index=False)

# تحلیل‌های پایه
# مثال: شمارش تعداد تکرار کلمات در توضیحات
repeated_items = get_repeated_items(descriptions)

# نمایش آیتم‌های تکراری
print("Repeated Items in Job Descriptions:")
for item, count in repeated_items.items():
    print(f"{item}: {count} times")

# تحلیل بیشتر با استفاده از پانداس
# مثال: پیدا کردن توضیحاتی که کلمه خاصی در آنها تکرار شده است
keyword = 'Laravel'
df['contains_keyword'] = df['description'].apply(lambda x: keyword in x)
print(df[df['contains_keyword']])

# مثال: نمایش توزیع طول توضیحات
df['description_length'] = df['description'].apply(len)
print(df['description_length'].describe())

# ترسیم نمودار طول توضیحات
df['description_length'].hist()
import matplotlib.pyplot as plt

plt.xlabel('Description Length')
plt.ylabel('Frequency')
plt.title('Distribution of Job Description Lengths')
plt.show()
